import json
import os
from threading import Thread
from chromecastplayer import ChromecastPlayer
from chromecastrequest import ChromecastRequest
from objectid import PydanticObjectId
from utils import initialize_chromecasts, jsonify_directory
from repository import DeviceRepository
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer


""" Flask and Repository Setup """

app = Flask("__main__")
CORS(app)

device_repository: DeviceRepository = DeviceRepository(app)


""" Chromecast Initialization """

global chromecasts
chromecasts: dict[PydanticObjectId,
                  ChromecastPlayer] = initialize_chromecasts(device_repository)


""" Error Handler """


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


""" Health """


@app.route("/health")
def index() -> Response:
    return "Success", 200


""" Chromecast Requests"""


@app.route("/update", methods=["PUT"])
def update_chromecasts() -> Response:
    global chromecasts
    chromecasts = initialize_chromecasts(device_repository)
    return "Success", 200


@app.route("/request/media", methods=["POST"])
def get_media() -> Response:
    try:
        chromecast_request = ChromecastRequest(**request.get_json())
        chromecast = chromecasts[chromecast_request.target]
        cast_thread = Thread(target=chromecast.cast_media,
                             args=(chromecast_request.path,))
        cast_thread.start()

        return "Success", 200

    except KeyError as e:
        return str(e), 404


@app.route("/media", methods=["GET"])
def get_media() -> Response:
    try:
        print(json.dumps(jsonify_directory("media")))
        return json.dumps(jsonify_directory("media")), 200

    except KeyError as e:
        return str(e), 404


if __name__ == "__main__":
    http_server = WSGIServer(("", 5000), app)
    http_server.serve_forever()
