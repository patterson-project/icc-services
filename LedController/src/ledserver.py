from flask import Flask, Response, request
from flask_cors import CORS
from utils import LightingRequest, log
from ledstrip import LedStripController

app: Flask = Flask("__main__")
CORS(app)

led_strip_controller: LedStripController = LedStripController()


@app.route("/health")
def index() -> Response:
    return Response("Healthy", status=200)


@app.route("/lightingrequest", methods=["POST"])
def led_strip() -> Response:
    body = request.get_json()
    led_request = LightingRequest(**body)
    log(led_request.__dict__)

    led_strip_controller.request = led_request
    led_strip_controller.operation_callback_by_name[led_request.operation]()
    return Response(status=200)


if __name__ == "__main__":
    app.run(host="", port=8000, threaded=True)
