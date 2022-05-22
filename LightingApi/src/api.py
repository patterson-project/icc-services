import requests
from flask import Flask, Response, redirect, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from utils import ServiceUris


app: Flask = Flask("__main__")
CORS(app)


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
        return "Error: " + str(e), 400


@app.route("/lighting/bulb2/status/on", methods=["GET"])
def bulb_2_on() -> Response:
    try:
        bulb_2_response: Response = requests.get(
            ServiceUris.BULB_SERVICE + "/status/on/bulb2"
        )
        return bulb_2_response.json(), 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


@app.route("/lighting/ledstrip/status/on", methods=["GET"])
def led_strip_on() -> Response:
    try:
        led_response: Response = requests.get(
            ServiceUris.LED_STRIP_SERVICE + "/status/on"
        )
        return led_response.json(), 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


@app.route("/lighting/ledstrip/request", methods=["POST"])
def led_strip() -> Response:
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/request", json=request.get_json()
        )
        return "Success", 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


@app.route("/lighting/bulb1/request", methods=["POST"])
def bulb_1() -> Response:
    try:
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb1", json=request.get_json()
        )
        return "Success", 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


@app.route("/lighting/bulb2/request", methods=["POST"])
def bulb_2() -> Response:
    try:
        requests.post(
            ServiceUris.BULB_SERVICE + "/request/bulb2", json=request.get_json()
        )
        return "Success", 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
