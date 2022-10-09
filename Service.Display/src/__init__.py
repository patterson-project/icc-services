from reverseproxy import ReverseProxy
from showrequest import ShowRequest
from movierequest import MovieRequest
from repository import AnalyticsRepository
from flask import Flask, Response, request, jsonify
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
    return 200


""" Display Requests """


@app.route("/displays/chromecast/movie", methods=["POST"])
def chromecast_request() -> Response:
    movie_request = MovieRequest(**request.get_json())

    rp = ReverseProxy()
    rp.chromecast_movie_request(movie_request)

    analytics_repository.save_movie_request(request)
    return 200


@app.route("/displays/chromecast/show", methods=["POST"])
def chromecast_request() -> Response:
    show_request = ShowRequest(**request.get_json())

    rp = ReverseProxy()
    rp.chromecast_show_request(show_request)

    analytics_repository.save_show_request(request)
    return 200


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
