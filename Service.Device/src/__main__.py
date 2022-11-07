from repository import DeviceRepository, StateRepository
from utils import update_controllers
from flask import Flask, Response, request, jsonify, abort
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from pymongo.errors import DuplicateKeyError
from icc.models import Device


""" Flask and Pymongo Setup """

app = Flask("__main__")
CORS(app)

device_repository: DeviceRepository = DeviceRepository(app)
state_repository: StateRepository = StateRepository(app)


""" Error Handlers"""


@app.errorhandler(404)
def resource_not_found(e) -> Response:
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def resource_not_found(e) -> Response:
    return jsonify(error=f"Duplicate key error."), 400


""" Health """


@app.route("/devices/health")
def index() -> Response:
    return "Healthy", 200


""" Device & State CRUD """


@app.route("/devices/states", methods=["GET"])
def get_all_states():
    all_states = state_repository.find_all()
    return jsonify(all_states)


@app.route("/devices", methods=["POST"])
def add_device() -> Response:
    new_device = device_repository.save(request)
    state_repository.save(new_device.inserted_id, False)

    device = Device(**request.get_json())
    update_controllers(device)

    return device.to_json()


@app.route("/devices", methods=["GET"])
def get_all_devices() -> Response:
    all_devices = device_repository.find_all()
    return jsonify(all_devices)


@app.route("/devices", methods=["PUT"])
def update_device() -> Response:
    updated_device = device_repository.update(request)

    if updated_device:
        device = Device(**request.get_json())
        update_controllers(device)
        return Device(**updated_device).to_json()
    else:
        abort(404, "Device not found")


@app.route("/devices/<string:id>", methods=["DELETE"])
def delete_device(id: str) -> Response:
    deleted_device = device_repository.delete(id)
    if deleted_device:
        device = Device(**deleted_device)
        update_controllers(device)
        state_repository.delete(id)
        return device.to_json()
    else:
        abort(404, "Device not found")


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
