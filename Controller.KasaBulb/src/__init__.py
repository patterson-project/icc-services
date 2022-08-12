import asyncio
import os
from threading import Thread
from bson import ObjectId
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from kasa import SmartDeviceException
from lightingrequest import LightingRequest
from bulb import BulbController
from gevent.pywsgi import WSGIServer
from device import Device
from state import State


# Flask app object with CORS
app = Flask("__main__")
CORS(app)

iotdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
devices: Collection = iotdb.db.devices
states: Collection = iotdb.db.states

analyticsdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
state_records: Collection = analyticsdb.db.states

# Global bulb controllers
bulbs: dict[ObjectId, BulbController] = {}

# Event loop for running bulb commands in a seperate thread
loop = asyncio.new_event_loop()


def get_bulb_devices():
    kasa_bulbs = list(
        Device(**device)
        for device in devices.find({"type": "Lighting", "model": "Kasa Bulb"})
    )

    for bulb in kasa_bulbs:
        bulb_controller = BulbController()
        asyncio.run_coroutine_threadsafe(
            bulb_controller.create_bulb(bulb.ip), loop)
        bulbs[bulb.id] = bulb_controller


""" Routes """


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/health")
def index() -> Response:
    return "Healthy", 200


@app.route("/update", methods=["PUT"])
def update_bulbs() -> Response:
    bulbs.clear()
    get_bulb_devices()
    return "Success", 200


@app.route("/request", methods=["POST"])
def lighting_request() -> Response:
    try:
        lighting_request = LightingRequest(**request.get_json())
        bulb_controller = bulbs[lighting_request.target]
        bulb_controller.set_request(lighting_request)
        asyncio.run_coroutine_threadsafe(
            bulb_controller.operation_callback_by_name[lighting_request.operation](
            ), loop
        )

        state: bool = None
        if lighting_request.operation != "off":
            state = True
        else:
            state = False

        states.find_one_and_update({"device": lighting_request.target}, {
            "$set": {"state": state}}, upsert=True)
        state_records.insert_one(
            State(device=lighting_request.target, state=state).to_bson())

        return "Success", 200

    except (SmartDeviceException, TypeError, KeyError) as e:
        return str(e), 500


def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == "__main__":
    get_bulb_devices()
    bulb_thread = Thread(target=start_background_loop,
                         args=(loop,), daemon=True)
    bulb_thread.start()

    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
