import requests
from flask import Flask, Response, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from config import ServiceUris


app: Flask = Flask("__main__")
CORS(app)


@app.route("/lighting/health", methods=["GET"])
def index() -> Response:
    return "Healthy", 200


@app.route("/lighting/ledstrip/request", methods=["POST"])
def led_strip() -> Response:
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=request.get_json()
        )
        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/bulb/request", methods=["POST"])
def bulb_1() -> Response:
    try:
        requests.post(ServiceUris.BULB_CONTROLLER + "/request", json=request.get_json())
        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


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
            ServiceUris.BULB_CONTROLLER + "/request/bulb1", json=bulb_1_ocean_request
        )
        requests.post(
            ServiceUris.BULB_CONTROLLER + "/request/bulb2", json=bulb_2_ocean_request
        )

        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/scene/rose", methods=["POST"])
def rose() -> Response:
    led_strip_rose_request = dict(operation="hsv", h=294, s=22, v=99)
    bulb_1_rose_request = dict(operation="hsv", h=301, s=55, v=98)
    bulb_2_rose_request = dict(operation="hsv", h=298, s=55, v=95)
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=led_strip_rose_request
        )
        requests.post(
            ServiceUris.BULB_CONTROLLER + "/request/bulb1", json=bulb_1_rose_request
        )
        requests.post(
            ServiceUris.BULB_CONTROLLER + "/request/bulb2", json=bulb_2_rose_request
        )

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
            ServiceUris.BULB_CONTROLLER + "/request/bulb1", json=bulb_1_rainbow_request
        )
        requests.post(
            ServiceUris.BULB_CONTROLLER + "/request/bulb2", json=bulb_2_rainbow_request
        )

        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/scene/candy", methods=["POST"])
def candy() -> Response:
    led_strip_candy_request = dict(operation="hsv", h=260, s=63, v=96)
    bulb_1_candy_request = dict(operation="hsv", h=301, s=55, v=98)
    bulb_2_candy_request = dict(operation="hsv", h=270, s=69, v=87)
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=led_strip_candy_request
        )
        requests.post(
            ServiceUris.BULB_CONTROLLER + "/request/bulb1", json=bulb_1_candy_request
        )
        requests.post(
            ServiceUris.BULB_CONTROLLER + "/request/bulb2", json=bulb_2_candy_request
        )

        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/scene/peachy", methods=["POST"])
def peachy() -> Response:
    led_strip_peachy_request = dict(operation="hsv", h=17, s=90, v=100)
    bulb_1_peachy_request = dict(operation="hsv", h=27, s=59, v=100)
    bulb_2_peachy_request = dict(operation="hsv", h=54, s=70, v=94)
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=led_strip_peachy_request
        )
        requests.post(
            ServiceUris.BULB_CONTROLLER + "/request/bulb1", json=bulb_1_peachy_request
        )
        requests.post(
            ServiceUris.BULB_CONTROLLER + "/request/bulb2", json=bulb_2_peachy_request
        )

        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


@app.route("/lighting/scene/jungle", methods=["POST"])
def jungle() -> Response:
    led_strip_jungle_request = dict(operation="hsv", h=66, s=100, v=100)
    bulb_1_jungle_request = dict(operation="hsv", h=95, s=100, v=100)
    bulb_2_jungle_request = dict(operation="hsv", h=136, s=100, v=34)
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=led_strip_jungle_request
        )
        requests.post(
            ServiceUris.BULB_CONTROLLER + "/request/bulb1", json=bulb_1_jungle_request
        )
        requests.post(
            ServiceUris.BULB_CONTROLLER + "/request/bulb2", json=bulb_2_jungle_request
        )

        return "Success", 200
    except requests.HTTPError as e:
        return str(e), 500


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
