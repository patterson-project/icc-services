import asyncio
import json
from threading import Thread
from bson import ObjectId
from quart import Quart, Response, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from kasa import SmartDeviceException
from lightingrequest import LightingRequest
from bulb import BulbController
from gevent.pywsgi import WSGIServer
from device import Device
from config import ServiceUris

# Flask app object with CORS
app = Quart("__main__")
app.config["MONGO_URI"] = ServiceUris.MONGO_DB_URI

CORS(app)
pymongo = PyMongo(app)

devices: Collection = pymongo.db.devices

# Global bulb controllers
bulbs: dict[ObjectId, BulbController] = {}

# Event loop for running bulb commands in a seperate thread
loop = asyncio.new_event_loop()


async def get_bulb_devices():
    kasa_bulbs = list(
        Device(**device)
        for device in devices.find({"type": "lighting", "model": "Kasa KL-215"})
    )

    for bulb in kasa_bulbs:
        bulb_controller = BulbController()
        asyncio.run_coroutine_threadsafe(bulb_controller.create_bulb(bulb.ip), loop)
        bulbs[bulb.id] = bulb_controller


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/health")
def index() -> Response:
    return "Healthy", 200


@app.route("/add/<string:id>", methods=["POST"])
async def add_bulb(id: str):
    new_bulb_id = ObjectId(id)
    new_bulb = Device(**devices.find_one_or_404({"_id": new_bulb_id}))
    bulb_controller = BulbController()
    await bulb_controller.create_bulb(new_bulb.ip)
    bulbs[new_bulb_id] = bulb_controller


@app.route("/update", methods=["PUT"])
def update_bulbs():
    get_bulb_devices()


@app.route("/request", methods=["POST"])
async def lighting_request() -> Response:
    try:
        bulb_request = LightingRequest(**json.loads(request.data))
        bulb_controller = bulbs[bulb_request.id]
        bulb_controller.set_request(bulb_request)
        await bulb_controller.update_bulb()
        await bulb_controller.operation_callback_by_name[bulb_request.operation]()
        return "Success", 200
    except (SmartDeviceException, TypeError) as e:
        return str(e), 500


def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == "__main__":
    get_bulb_devices()
    bulb_thread = Thread(target=start_background_loop, args=(loop,), daemon=True)
    bulb_thread.start()

    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
