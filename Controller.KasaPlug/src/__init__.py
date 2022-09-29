import asyncio
import os
from threading import Thread
from bson import ObjectId
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from kasa import SmartDeviceException
from powerrequest import PowerRequest
from plug import Plug
from gevent.pywsgi import WSGIServer
from device import Device
from state import State


# Flask app object with CORS
app = Flask("__main__")
CORS(app)

# Databases
iotdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
devices: Collection = iotdb.db.devices
states: Collection = iotdb.db.states

analyticsdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
state_records: Collection = analyticsdb.db.states

# Global plug dictionary
plugs: dict[ObjectId, Plug] = {}

# Event loop for running bulb commands in a seperate thread
loop = asyncio.new_event_loop()


def get_plug_devices():
    kasa_plugs = list(
        Device(**device)
        for device in devices.find({"type": "Power", "model": "Kasa Plug"})
    )

    for plug_device in kasa_plugs:
        plug = Plug()
        asyncio.run_coroutine_threadsafe(
            plug.create_plug(plug_device.ip), loop)
        plugs[plug_device.id] = plug


""" Routes """


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/health")
def index() -> Response:
    return "Healthy", 200


@app.route("/update", methods=["PUT"])
def update_bulbs() -> Response:
    plugs.clear()
    get_plug_devices()
    return "Success", 200


@app.route("/request", methods=["POST"])
def lighting_request() -> Response:
    try:
        power_request: PowerRequest = PowerRequest(**request.get_json())
        plug: Plug = plugs[power_request.target]
        plug.set_request(power_request)

        asyncio.run_coroutine_threadsafe(
            plug.operation_callback_by_name[power_request.operation](
            ), loop
        )

        state: bool = False
        if power_request.operation != "off":
            state = True

        states.find_one_and_update({"device": power_request.target}, {
            "$set": {"state": state}}, upsert=True)
        state_records.insert_one(
            State(device=power_request.target, state=state).to_bson())

        return "Success", 200

    except (SmartDeviceException, TypeError, KeyError) as e:
        return str(e), 500


def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == "__main__":
    get_plug_devices()
    strip_thread = Thread(target=start_background_loop,
                          args=(loop,), daemon=True)
    strip_thread.start()

    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
