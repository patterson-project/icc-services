import os
from powerrequest import PowerRequest
import requests
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import ObjectId
from gevent.pywsgi import WSGIServer
from pymongo.collection import Collection, ReturnDocument
from pymongo.errors import DuplicateKeyError
from repository import insert_power_request
from device import Device
from reverseproxy import ReverseProxy


""" Flask and Pymongo Setup """


app: Flask = Flask("__main__")
CORS(app)

analyticsdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
power_requests: Collection = analyticsdb.db.power_requests

iotdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
devices: Collection = iotdb.db.devices


""" Error Handlers """


@app.errorhandler(404)
def resource_not_found(e) -> Response:
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def resource_not_found(e) -> Response:
    return jsonify(error=f"Duplicate key error."), 400


""" Health """


@app.route("/power/health", methods=["GET"])
def index() -> Response:
    return "Healthy", 200


""" Lighting Requests """


@app.route("/power/request/id", methods=["POST"])
def id_request() -> Response:
    try:
        power_request = PowerRequest(**request.get_json())
        device = Device(**devices.find_one({"_id": power_request.target}))

        rp = ReverseProxy(device)
        rp.handle(power_request)

        insert_power_request(power_requests, request)

        return "Success", 200

    except requests.HTTPError as e:
        return str(e), e.errno


@app.route("/power/request/name", methods=["POST"])
def name_request() -> Response:
    try:
        power_request = PowerRequest(**request.get_json())
        device = Device(**devices.find_one({"name": power_request.name}))
        power_request.target = device.id

        rp = ReverseProxy(device)
        rp.handle(power_request)

        insert_power_request(power_requests, request)

        return "Success", 200

    except requests.HTTPError as e:
        return str(e), e.errno


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
