from powerrequest import PowerRequest
import requests
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from pymongo.errors import DuplicateKeyError
from repository import AnalyticsRepository, DeviceRepository
from reverseproxy import ReverseProxy


""" Flask and Pymongo Setup """

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

@app.route("/power/health", methods=["GET"])
def index() -> Response:
    return "Healthy", 200


""" Lighting Requests """

@app.route("/power/request/id", methods=["POST"])
def id_request() -> Response:
    try:
        power_request = PowerRequest(**request.get_json())
        device = device_repository.find_by_id(power_request.target)

        rp = ReverseProxy(device)
        rp.handle(power_request)

        analytics_repository.save_power_request(request)
        return "Success", 200

    except requests.HTTPError as e:
        return str(e), e.errno


@app.route("/power/request/name", methods=["POST"])
def name_request() -> Response:
    try:
        power_request = PowerRequest(**request.get_json())
        device = device_repository.find_by_name(power_request.name)
        power_request.target = device.id

        rp = ReverseProxy(device)
        rp.handle(power_request)

        analytics_repository.save_power_request(request)
        return "Success", 200

    except requests.HTTPError as e:
        return str(e), e.errno


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
