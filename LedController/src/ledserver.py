import json
import os
from flask import Flask, Response, request
from flask_cors import CORS
from utils import LedStripStatus, LightingRequest, ServiceUris
from ledstrip import LedStripController
from gevent.pywsgi import WSGIServer
from pymongo import MongoClient

app: Flask = Flask("__main__")
CORS(app)

led_strip: LedStripController = LedStripController()

mongo_client = MongoClient(
    f'mongodb://{os.environ["MONGO_DB_USERNAME"]}:{os.environ["MONGO_DB_PASSWORD"]}@{ServiceUris.MONGO_DB}'
)

iotdb = mongo_client["iot"]
device_states_collection = iotdb["device-states"]


def update_lighting_state(request: LightingRequest):
    query = {"device_name": "ledstrip"}

    if request.operation == "off":
        on = False
    else:
        on = True

    new_value = {"$set": {"on": on}}
    device_states_collection.update_one(query, new_value)


@app.route("/health")
def index() -> Response:
    return "Healthy", 200


@app.route("/request", methods=["POST"])
def lighting_request() -> Response:
    try:
        lighting_request = LightingRequest(**json.loads(request.data))
        led_strip.set_request(lighting_request)
        led_strip.operation_callback_by_name[lighting_request.operation]()
        update_lighting_state(lighting_request)
        return "Success", 200
    except TypeError as e:
        return str(e), 500


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
