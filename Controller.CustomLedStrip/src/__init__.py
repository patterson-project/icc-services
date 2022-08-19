import json
import os
from flask import Flask, Response, request
from flask_cors import CORS
from lightingrequest import LightingRequest
from ledstrip import LedStripController
from gevent.pywsgi import WSGIServer
from pymongo.collection import Collection
from state import State
from flask_pymongo import PyMongo


app: Flask = Flask("__main__")
CORS(app)

iotdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
states: Collection = iotdb.db.states

analyticsdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
state_records: Collection = analyticsdb.db.states


led_strip: LedStripController = LedStripController()


@app.route("/health")
def index() -> Response:
    return "Healthy", 200


@app.route("/request", methods=["POST"])
def lighting_request() -> Response:
    try:
        lighting_request = LightingRequest(**json.loads(request.data))

        led_strip.set_request(lighting_request)
        led_strip.operation_callback_by_name[lighting_request.operation]()

        state: bool = False
        if lighting_request.operation != "off":
            state = True

        states.find_one_and_update({"device": lighting_request.target}, {
            "$set": {"state": state}}, upsert=True)
        state_records.insert_one(
            State(device=lighting_request.target, state=state).to_bson())

        return "Success", 200

    except TypeError as e:
        return str(e), 500


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
