import json
from flask import Flask, Response, request
from flask_cors import CORS
from utils import LedStripStatus, LightingRequest
from ledstrip import LedStripController
from gevent.pywsgi import WSGIServer

app: Flask = Flask("__main__")
CORS(app)

led_strip: LedStripController = LedStripController()


@app.route("/health")
def index() -> Response:
    return "Healthy", 200


@app.route("/status/on", methods=["GET"])
def on() -> Response:
    led_strip_status = LedStripStatus(led_strip.is_on())
    return led_strip_status.__dict__, 200


@app.route("/request", methods=["POST"])
def lighting_request() -> Response:
    try:
        lighting_request = LightingRequest(**json.loads(request.data))
        led_strip.set_request(lighting_request)
        led_strip.operation_callback_by_name[lighting_request.operation]()
        return "Success", 200
    except TypeError as e:
        return str(e), 500


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
