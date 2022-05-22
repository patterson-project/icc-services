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
async def bulb_1_on() -> Response:
    try:
        bulb_1_response: Response = await requests.get(
            ServiceUris.BULB_SERVICE + "/on/bulb1"
        )
        return Response(response=bulb_1_response.get_json(), status=200)
    except requests.HTTPError as e:
        return Response(response="Error: " + str(e), status=400)


@app.route("/lighting/ledstrip", methods=["POST"])
def led_strip() -> Response:
    try:
        requests.post(
            ServiceUris.LED_STRIP_SERVICE + "/lightingrequest", json=request.get_json()
        )
        return Response(status=200)
    except requests.HTTPError as e:
        return Response(response="Error: " + str(e), status=400)


@app.route("/lighting/bulb1", methods=["POST"])
def bulb_1() -> Response:
    try:
        requests.post(
            ServiceUris.BULB_SERVICE + "/lightingrequest/bulb1", json=request.get_json()
        )
        return Response(status=200)
    except requests.HTTPError as e:
        return Response(response="Error: " + str(e), status=400)


@app.route("/lighting/bulb2", methods=["POST"])
def bulb_2() -> Response:
    try:
        requests.post(
            ServiceUris.BULB_SERVICE + "/lightingrequest/bulb2", json=request.get_json()
        )
        return Response(status=200)
    except requests.HTTPError as e:
        return Response(response="Error: " + str(e), status=400)


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
