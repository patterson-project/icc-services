import requests
from reverseproxy import ReverseProxy
from chromecastrequest import ChromecastRequest
from repository import AnalyticsRepository
from flask import Flask, Response, request, jsonify
from config import Config
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from pymongo.errors import DuplicateKeyError


""" Flask and Repository Setup """

app: Flask = Flask("__main__")
CORS(app)

analytics_repository: AnalyticsRepository = AnalyticsRepository(app)


""" Error Handlers """


@app.errorhandler(404)
def resource_not_found(e) -> Response:
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def resource_not_found(e) -> Response:
    return jsonify(error=f"Duplicate key error."), 400


""" Health """


@app.route("/displays/health", methods=["GET"])
def index() -> Response:
    return "Success", 200


""" Display Requests """


@app.route("/displays/chromecast/media", methods=["POST"])
def chromecast_media_request() -> Response:
    chromecast_request = ChromecastRequest(**request.get_json())

    rp = ReverseProxy()
    response = rp.media_request(chromecast_request)

    analytics_repository.save_chromecast_request(request)
    return (response.content, response.status_code, response.headers.items())


@app.route("/displays/chromecast/media", methods=["GET"])
def get_all_media() -> Response:
    rp = ReverseProxy()
    response = rp.media_request()

    analytics_repository.save_chromecast_request(request)
    return (response.content, response.status_code, response.headers.items())


@app.route("/displays/chromecast/update", methods=["PUT"])
def update_chromecasts():
    response = requests.put(Config.CHROMECAST_CONTROLLER_URL)
    return (response.content, response.status_code, response.headers.items())


@app.route("/displays/videos/shows", methods=["GET"])
def get_all_shows() -> None:
    # return list of shows each with a title and list of seasons & episodes
    pass


@app.route("/displays/videos/movies", methods=["GET"])
def get_all_movies() -> None:
    # return list of movies each with a title
    pass


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
