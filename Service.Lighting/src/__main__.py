import requests
from repository import AnalyticsRepository, DeviceRepository
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from pymongo.errors import DuplicateKeyError
from icc.models import LightingRequest
from reverseproxy import ReverseProxy


""" Flask and Repository Setup """

app: Flask = Flask("__main__")
CORS(app)

device_repository: DeviceRepository = DeviceRepository(app)
analytics_repository: AnalyticsRepository = AnalyticsRepository(app)


""" Error Handlers """


@app.errorhandler(404)
def resource_not_found(e) -> Response:
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def resource_not_found(e) -> Response:
    return jsonify(error=f"Duplicate key error."), 400


""" Health """


@app.route("/lighting/health", methods=["GET"])
def index() -> Response:
    return "Healthy", 200


""" Lighting Requests """


@app.route("/lighting/request/id", methods=["POST"])
def id_request() -> Response:
    try:
        lighting_request = LightingRequest(**request.get_json())
        device = device_repository.find_by_id(lighting_request.target)

        rp = ReverseProxy(device)
        response = rp.handle(lighting_request)

        analytics_repository.save_lighting_request(request)
        return (response.content, response.status_code, response.headers.items())

    except requests.HTTPError as e:
        return str(e), e.errno


@app.route("/lighting/request/name", methods=["POST"])
def name_request() -> Response:
    try:
        lighting_request = LightingRequest(**request.get_json())
        device = device_repository.find_by_name(lighting_request.name)

        lighting_request.target = device.id

        rp = ReverseProxy(device)
        response = rp.handle(lighting_request)

        analytics_repository.save_lighting_request(request)
        return (response.content, response.status_code, response.headers.items())

    except requests.HTTPError as e:
        return str(e), e.errno


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
