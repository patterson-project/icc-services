import os
from bson import ObjectId
from flask import Flask, Response, request, jsonify, abort
from flask_cors import CORS
from flask_pymongo import PyMongo
from gevent.pywsgi import WSGIServer
from pymongo.collection import Collection, ReturnDocument
from pymongo.errors import DuplicateKeyError
from model import Device

app = Flask("__main__")
app.config[
    "MONGO_URI"
] = f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin"

CORS(app)
pymongo = PyMongo(app)

devices: Collection = pymongo.db.devices


@app.errorhandler(404)
def resource_not_found(e) -> Response:
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def resource_not_found(e) -> Response:
    return jsonify(error=f"Duplicate key error."), 400


@app.route("/devices/health")
def index() -> Response:
    return "Healthy", 200


@app.route("/devices", methods=["POST"])
def new_device() -> Response:
    raw_device = request.get_json()
    device = Device(**raw_device)
    devices.insert_one(device.to_bson())
    return device.to_json()


@app.route("/devices", methods=["GET"])
def get_all_devices() -> Response:
    all_devices = list(Device(**device).to_json() for device in devices.find())
    return jsonify(all_devices)


@app.route("/devices", methods=["PUT"])
def update_device() -> Response:
    device = Device(**request.get_json())
    updated_device = devices.find_one_and_update(
        {"_id": device.id},
        {"$set": device.to_bson()},
        return_document=ReturnDocument.AFTER,
    )
    if update_device:
        return Device(**updated_device).to_json()
    else:
        abort(404, "Device not found")


@app.route("/devices/<string:id>", methods=["DELETE"])
def delete_device(id: str) -> Response:
    deleted_device = devices.find_one_and_delete({"_id": ObjectId(id)})
    if deleted_device:
        return Device(**deleted_device).to_json()
    else:
        abort(404, "Device not found")


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
