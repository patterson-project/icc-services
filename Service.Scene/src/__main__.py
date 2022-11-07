import requests
from repository import AnalyticsRepository, DeviceRepository, SceneRepository
from flask import Flask, Response, request, jsonify, abort
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from pymongo.errors import DuplicateKeyError
from reverseproxy import ReverseProxy
from icc.models import Scene, SceneRequest


""" Flask and Repository Setup """

app: Flask = Flask("__main__")
CORS(app)

device_repository: DeviceRepository = DeviceRepository(app)
analytics_repository: AnalyticsRepository = AnalyticsRepository(app)
scene_repository: SceneRepository = SceneRepository(app)


""" Error Handlers """


@app.errorhandler(404)
def resource_not_found(e) -> Response:
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def resource_not_found(e) -> Response:
    return jsonify(error=f"Duplicate key error."), 400


""" Health """


@app.route("/scenes/health", methods=["GET"])
def index() -> Response:
    return "Healthy", 200


""" Scene Requests """


@app.route("/scenes/request", methods=["POST"])
def scene_request() -> Response:
    try:
        scene_request = SceneRequest(**request.get_json())
        scene = Scene(**scene_repository.find_by_name(scene_request.name))

        for lighting_request in scene.lighting_requests:
            device = device_repository.find_by_id(lighting_request.target)

            rp = ReverseProxy(device)
            rp.handle(lighting_request)

        for power_request in scene.power_requests:
            device = device_repository.find_by_id(lighting_request.target)

            rp = ReverseProxy(device)
            rp.handle(power_request)

        analytics_repository.save_scene_request(request)
        return "Success", 200

    except requests.HTTPError as e:
        return str(e), e.errno


""" Scene CRUD """


@ app.route("/scenes", methods=["POST"])
def add_scene() -> Response:
    scene_repository.save(request)
    return request.to_json()


@ app.route("/scenes", methods=["GET"])
def get_all_scenes() -> Response:
    all_scenes = scene_repository.find_all()
    return jsonify(all_scenes)


@ app.route("/scenes", methods=["PUT"])
def update_scene() -> Response:
    updated_scene = scene_repository.update(request)
    if updated_scene:
        return Scene(**updated_scene).to_json()
    else:
        abort(404, "Scene not found")


@ app.route("/scenes/<string:id>", methods=["DELETE"])
def delete_device(id: str) -> Response:
    deleted_scene = scene_repository.delete(id)
    if deleted_scene:
        scene = Scene(**deleted_scene)
        return scene.to_json()
    else:
        abort(404, "Scene not found")


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
