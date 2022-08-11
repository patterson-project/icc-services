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
from ledstrip import LedStripController
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
strips: dict[ObjectId, LedStripController] = {}

# Event loop for running bulb commands in a seperate thread
loop = asyncio.new_event_loop()


def get_led_strip_devices():
    kasa_led_strips = list(
        Device(**device)
        for device in devices.find({"type": "Lighting", "model": "Kasa Led Strip"})
    )

    for strip in kasa_led_strips:
        led_strip_controller = LedStripController()
        asyncio.run_coroutine_threadsafe(
            led_strip_controller.create_strip(strip.ip), loop)
        strips[strip.id] = led_strip_controller


""" Routes """


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/health")
def index() -> Response:
    return "Healthy", 200


@app.route("/update", methods=["PUT"])
def update_bulbs() -> Response:
    strips.clear()
    get_led_strip_devices()
    return "Success", 200


@app.route("/request", methods=["POST"])
def lighting_request() -> Response:
    try:
        lighting_request = LightingRequest(**request.get_json())
        led_strip_controller = strips[lighting_request.target]
        led_strip_controller.set_request(lighting_request)
        asyncio.run_coroutine_threadsafe(
            led_strip_controller.update_strip(), loop)
        asyncio.run_coroutine_threadsafe(
            led_strip_controller.operation_callback_by_name[lighting_request.operation](
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
    get_led_strip_devices()
    strip_thread = Thread(target=start_background_loop,
                          args=(loop,), daemon=True)
    strip_thread.start()

    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
