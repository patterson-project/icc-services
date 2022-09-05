import os
import requests
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from gevent.pywsgi import WSGIServer
from config import Config
from pymongo.collection import Collection
from pymongo.errors import DuplicateKeyError
from repository import insert_lighting_request
from device import Device, LightingDeviceTypes
from lightingrequest import LightingRequest
from reverseproxy import ReverseProxy


app: Flask = Flask("__main__")
CORS(app)

analyticsdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
lighting_requests: Collection = analyticsdb.db.lighting_requests

iotdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
devices: Collection = iotdb.db.devices


@app.errorhandler(404)
def resource_not_found(e) -> Response:
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def resource_not_found(e) -> Response:
    return jsonify(error=f"Duplicate key error."), 400


@app.route("/lighting/health", methods=["GET"])
def index() -> Response:
    return "Healthy", 200


@app.route("/lighting/request/id", methods=["POST"])
def id_request() -> Response:
    try:
        lighting_request = LightingRequest(**request.get_json())
        device = Device(**devices.find_one({"_id": lighting_request.target}))

        rp = ReverseProxy(device)
        rp.handle(request)

        insert_lighting_request(lighting_requests, request)

        return "Success", 200

    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/request/name", methods=["POST"])
def name_request() -> Response:
    try:
        lighting_request = LightingRequest(**request.get_json())
        device = Device(**devices.find_one({"name": lighting_request.name}))

        rp = ReverseProxy(device)
        rp.handle(request)

        insert_lighting_request(lighting_requests, request)

        return "Success", 200

    except requests.HTTPError as e:
        return str(e), 500


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
