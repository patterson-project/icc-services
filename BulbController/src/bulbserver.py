import asyncio
import os
import json
from threading import Thread
from flask import Flask, Response, request
from flask_cors import CORS
from kasa import SmartDeviceException
from utils import LightingRequest, ServiceUris
from bulb import BulbController
from gevent.pywsgi import WSGIServer
from pymongo import MongoClient

# Flask app object with CORS
app: Flask = Flask("__main__")
CORS(app)

# Global bulb controllers
bulb_1: BulbController = BulbController()
bulb_2: BulbController = BulbController()

# Event loop for running bulb commands in a seperate thread
loop = asyncio.new_event_loop()

mongo_client = MongoClient(
    f'mongodb://{os.environ["MONGO_DB_USERNAME"]}:{os.environ["MONGO_DB_PASSWORD"]}@{ServiceUris.MONGO_DB}'
)

iotdb = mongo_client["iot"]
device_states_collection = iotdb["device-states"]


def update_lighting_state(device_name: str, request: LightingRequest):
    query = {"device_name": device_name}

    if request.operation == "off":
        on = False
    else:
        on = True

    new_value = {"$set": {"on": on}}
    device_states_collection.update_one(query, new_value)


@app.route("/health")
def index() -> Response:
    return "Healthy", 200


@app.route("/request/bulb1", methods=["POST"])
async def lighting_request_bulb_1() -> Response:
    try:
        bulb_request = LightingRequest(**json.loads(request.data))
        bulb_1.set_request(bulb_request)
        asyncio.run_coroutine_threadsafe(bulb_1.update_bulb(), loop)
        asyncio.run_coroutine_threadsafe(
            bulb_1.operation_callback_by_name[bulb_request.operation](), loop
        )
        update_lighting_state(device_name="bulb1", request=bulb_request)
        return "Success", 200
    except (SmartDeviceException, TypeError) as e:
        return str(e), 500


@app.route("/request/bulb2", methods=["POST"])
async def lighting_request_bulb_2() -> Response:
    try:
        bulb_request = LightingRequest(**json.loads(request.data))
        bulb_2.set_request(bulb_request)
        asyncio.run_coroutine_threadsafe(bulb_2.update_bulb(), loop)
        asyncio.run_coroutine_threadsafe(
            bulb_2.operation_callback_by_name[bulb_request.operation](), loop
        )
        update_lighting_state(device_name="bulb2", request=bulb_request)
        return "Success", 200
    except (SmartDeviceException, TypeError) as e:
        return str(e), 500


def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == "__main__":
    bulb_thread = Thread(target=start_background_loop, args=(loop,), daemon=True)
    bulb_thread.start()

    asyncio.run_coroutine_threadsafe(bulb_1.create_bulb(os.environ["BULB_1_IP"]), loop)
    asyncio.run_coroutine_threadsafe(bulb_2.create_bulb(os.environ["BULB_2_IP"]), loop)

    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
