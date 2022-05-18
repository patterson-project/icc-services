from flask import Flask, Response, request
from flask_cors import CORS
from utils import LightingRequest, log
from bulb import BulbController
from gevent.pywsgi import WSGIServer

app: Flask = Flask("__main__")
CORS(app)

bulb_controller: BulbController = BulbController()


@app.route("/health")
def index() -> Response:
    return Response("Healthy", status=200)


@app.route("/lightingrequest", methods=["POST"])
async def led_strip() -> Response:
    body = request.get_json()
    bulb_request = LightingRequest(**body)
    log(bulb_request.__dict__)

    bulb_controller.request = bulb_request
    await bulb_controller.operation_callback_by_name[bulb_request.operation]()
    return Response(status=200)


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
