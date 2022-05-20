import json
from flask import Flask, Response, request
from flask_cors import CORS
from utils import LightingRequest
from ledstrip import LedStripController
from gevent.pywsgi import WSGIServer

app: Flask = Flask("__main__")
CORS(app)

led_strip_controller: LedStripController = LedStripController()


@app.route("/health")
def index() -> Response:
    return Response("Healthy", status=200)


@app.route("/lightingrequest", methods=["POST"])
def led_strip() -> Response:
    led_request = LightingRequest(**json.loads(request.data))
    led_strip_controller.request = led_request

    led_strip_controller.operation_callback_by_name[led_request.operation]()
    return Response(status=200)


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
