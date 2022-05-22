import requests
from flask import Flask, Response, redirect, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from utils import ServiceUris


app: Flask = Flask("__main__")
CORS(app)


@app.route("/lighting/health")
def index() -> Response:
    return Response("Healthy", status=200)


@app.route("/status/on/bulb1", methods=["GET"])
def bulb_1_on() -> Response:
    try:
        bulb_1_response: Response = requests.get(ServiceUris.BULB_SERVICE + "/on/bulb1")
        return bulb_1_response.json(), 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


@app.route("/status/on/bulb2", methods=["GET"])
def bulb_2_on() -> Response:
    try:
        bulb_2_response: Response = requests.get(ServiceUris.BULB_SERVICE + "/on/bulb2")
        return bulb_2_response.json(), 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


@app.route("/status/on/ledstrip", methods=["GET"])
def led_strip_on() -> Response:
    try:
        led_response: Response = requests.get(ServiceUris.LED_STRIP_SERVICE + "/on")
        return led_response.json(), 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


@app.route("/lighting/ledstrip", methods=["POST"])
def led_strip() -> Response:
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/lightingrequest", json=request.get_json()
        )
        return "Success", 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


@app.route("/lighting/bulb1", methods=["POST"])
def bulb_1() -> Response:
    try:
        requests.post(
            ServiceUris.BULB_SERVICE + "/lightingrequest/bulb1", json=request.get_json()
        )
        return "Success", 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


@app.route("/lighting/bulb2", methods=["POST"])
def bulb_2() -> Response:
    try:
        requests.post(
            ServiceUris.BULB_SERVICE + "/lightingrequest/bulb2", json=request.get_json()
        )
        return "Success", 200
    except requests.HTTPError as e:
        return "Error: " + str(e), 400


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
