import requests
import os
from flask import Flask, Response, Request, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from utils import LightingRequestRecord, ServiceUris
from pymongo import MongoClient


app: Flask = Flask("__main__")
CORS(app)

mongo_client = MongoClient(
    f'mongodb://{os.environ["MONGO_DB_USERNAME"]}:{os.environ["MONGO_DB_PASSWORD"]}@{ServiceUris.DEVICE_DB}'
)

if os.environ["APP_ENV"] == "production":
    devicesdb = mongo_client["iot-devices"]
else:
    devicesdb = mongo_client["iot-devices-dev"]

lighting_requests_collection = devicesdb["lighting-requests"]


def insert_lighting_request(request: Request):
    lighting_request = LightingRequestRecord(**request.get_json())
    lighting_requests_collection.insert_one(lighting_request.__dict__)


@app.route("/lighting/health", methods=["GET"])
def index() -> Response:
    return "Healthy", 200


@app.route("/lighting/bulb1/status/on", methods=["GET"])
def bulb_1_on() -> Response:
    try:
        bulb_1_response: Response = requests.get(
            ServiceUris.BULB_SERVICE + "/status/on/bulb1"
        )
        return bulb_1_response.json(), 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/bulb2/status/on", methods=["GET"])
def bulb_2_on() -> Response:
    try:
        bulb_2_response: Response = requests.get(
            ServiceUris.BULB_SERVICE + "/status/on/bulb2"
        )
        return bulb_2_response.json(), 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/ledstrip/status/on", methods=["GET"])
def led_strip_on() -> Response:
    try:
        led_response: Response = requests.get(
            ServiceUris.LED_STRIP_SERVICE + "/status/on"
        )
        return led_response.json(), 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/ledstrip/request", methods=["POST"])
def led_strip() -> Response:
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=request.get_json()
        )
        insert_lighting_request(request=request)
        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/bulb1/request", methods=["POST"])
def bulb_1() -> Response:
    try:
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb1", json=request.get_json()
        )
        insert_lighting_request(request=request)

        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/bulb2/request", methods=["POST"])
def bulb_2() -> Response:
    try:
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb2", json=request.get_json()
        )
        insert_lighting_request(request=request)
        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
