from readline import insert_text
import requests
import os
from flask import Flask, Response, Request, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from utils import DeviceState, LightingRequestRecord, ServiceUris
from pymongo import MongoClient


app: Flask = Flask("__main__")
CORS(app)

mongo_client = MongoClient(
    f'mongodb://{os.environ["MONGO_DB_USERNAME"]}:{os.environ["MONGO_DB_PASSWORD"]}@{ServiceUris.MONGO_DB}'
)

if os.environ["APP_ENV"] == "production":
    iotdb = mongo_client["iot"]
else:
    iotdb = mongo_client["iot-dev"]

lighting_requests_collection = iotdb["lighting-requests"]
device_states_collection = iotdb["device-states"]


def insert_lighting_request(device_name: str, request: Request):
    lighting_request = LightingRequestRecord(
        device_name=device_name, **request.get_json()
    )
    lighting_requests_collection.insert_one(lighting_request.__dict__)


def get_on_status(device_name: str) -> bool:
    return device_states_collection.find_one({"device_name": device_name})["on"]


@app.route("/lighting/health", methods=["GET"])
def index() -> Response:
    return "Healthy", 200


@app.route("/lighting/bulb1/status/on", methods=["GET"])
def bulb_1_on() -> Response:
    try:
        on = get_on_status(device_name="bulb1")
        return DeviceState(on).__dict__, 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/bulb2/status/on", methods=["GET"])
def bulb_2_on() -> Response:
    try:
        on = get_on_status(device_name="bulb2")
        return DeviceState(on).__dict__, 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/ledstrip/status/on", methods=["GET"])
def led_strip_on() -> Response:
    try:
        on = get_on_status(device_name="ledstrip")
        return DeviceState(on).__dict__, 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/ledstrip/request", methods=["POST"])
def led_strip() -> Response:
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=request.get_json()
        )
        insert_lighting_request(device_name="ledstrip", request=request)
        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/bulb1/request", methods=["POST"])
def bulb_1() -> Response:
    try:
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb1", json=request.get_json()
        )
        insert_lighting_request(device_name="bulb1", request=request)
        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/bulb2/request", methods=["POST"])
def bulb_2() -> Response:
    try:
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb2", json=request.get_json()
        )
        insert_lighting_request(device_name="bulb2", request=request)
        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


"""
1. Define scene route
2. In route function, define HSV lighting requests
3. Post each HSV request to each service
"""


@app.route("/lighting/scene/ocean", methods=["POST"])
def ocean() -> Response:
    led_strip_ocean_request = dict(operation="hsv", h=149, s=57, v=100)
    bulb_1_ocean_request = dict(operation="hsv", h=207, s=79, v=100)
    bulb_2_ocean_request = dict(operation="hsv", h=240, s=79, v=100)
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=led_strip_ocean_request
        )
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb1", json=bulb_1_ocean_request
        )
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb2", json=bulb_2_ocean_request
        )
        insert_lighting_request(device_name="ledstrip", request=request)
        insert_lighting_request(device_name="bulb1", request=request)
        insert_lighting_request(device_name="bulb2", request=request)
        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/scene/rose", methods=["POST"])
def rose() -> Response:
    led_strip_rose_request = dict(operation="hsv", h=294, s=22, v=99)
    bulb_1_rose_request = dict(operation="hsv", h=301, s=55, v=98)
    bulb_2_rose_request = dict(operation="hsv", h=288, s=57, v=95)
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=led_strip_rose_request
        )
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb1", json=bulb_1_rose_request
        )
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb2", json=bulb_2_rose_request
        )
        insert_lighting_request(device_name="ledstrip", request=request)
        insert_lighting_request(device_name="bulb1", request=request)
        insert_lighting_request(device_name="bulb2", request=request)
        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/scene/rainbow", methods=["POST"])
def rainbow() -> Response:
    led_strip_rainbow_request = dict(operation="rainbow")
    bulb_1_rainbow_request = dict(operation="rainbow")
    bulb_2_rainbow_request = dict(operation="rainbow")
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=led_strip_rainbow_request
        )
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb1", json=bulb_1_rainbow_request
        )
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb2", json=bulb_2_rainbow_request
        )
        insert_lighting_request(device_name="ledstrip", request=request)
        insert_lighting_request(device_name="bulb1", request=request)
        insert_lighting_request(device_name="bulb2", request=request)
        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
