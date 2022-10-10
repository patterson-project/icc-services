import asyncio
import os
from threading import Thread
from chromecastplayer import ChromecastPlayer
from showrequest import ShowRequest
from movierequest import MovieRequest
from objectid import PydanticObjectId
from utils import initialize_chromecasts, start_background_loop
from repository import DeviceRepository
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from gevent.pywsgi import WSGIServer


""" Flask and Repository Setup """

app = Flask("__main__")
CORS(app)

device_repository: DeviceRepository = DeviceRepository(app)


""" Chromecast Initialization """

loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
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


""" Bulb Requests"""


@app.route("/update", methods=["PUT"])
def update_chromecasts() -> Response:
    global chromecasts
    chromecasts = initialize_chromecasts(device_repository)
    return "Success", 200


@app.route("/request/movie", methods=["POST"])
def movie_request() -> Response:
    try:
        movie_request = MovieRequest(**request.get_json())
        movie_path = os.path.join(
            "mnt/media", "Movies", movie_request.movie_title)

        if not os.path.exists(movie_path):
            raise OSError("Movie not found")

        chromecast = chromecasts[movie_request.target]
        asyncio.run_coroutine_threadsafe(
            chromecast.cast_media(movie_path), loop)

        return "Success", 200

    except KeyError as e:
        return str(e), 404
    except OSError as e:
        return str(e), 404


@app.route("/request/show", methods=["POST"])
def show_request() -> Response:
    try:
        show_request = ShowRequest(**request.get_json())
        episode_path = os.path.join(
            "mnt/media", "Shows", show_request.show_title, show_request.season, show_request.episode)

        if not os.path.exists(episode_path):
            raise OSError("Show not found")

        chromecast = chromecasts[movie_request.target]
        asyncio.run_coroutine_threadsafe(
            chromecast.cast_media(episode_path), loop)

        return "Success", 200

    except KeyError as e:
        return str(e), 404
    except OSError as e:
        return str(e), 404


if __name__ == "__main__":
    cast_thread = Thread(target=start_background_loop,
                         args=(loop,), daemon=True)
    cast_thread.start()
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
