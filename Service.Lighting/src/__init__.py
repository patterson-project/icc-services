import requests
from lightingrepository import AnalyticsRepository, DeviceRepository, SceneRepository
from flask import Flask, Response, request, jsonify, abort
from flask_cors import CORS
from gevent.pywsgi import WSGIServer
from pymongo.collection import ReturnDocument
from pymongo.errors import DuplicateKeyError
from scenerequest import Scene, SceneRequest
from lightingrequest import LightingRequest
from reverseproxy import ReverseProxy


""" Flask and Pymongo Setup """


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
        rp.handle(lighting_request)

        analytics_repository.save_lighting_request(request)
        return "Success", 200

    except requests.HTTPError as e:
        return str(e), e.errno


@app.route("/lighting/request/name", methods=["POST"])
def name_request() -> Response:
    try:
        lighting_request = LightingRequest(**request.get_json())
        device = device_repository.find_by_name(lighting_request.name)

        lighting_request.target = device.id

        rp = ReverseProxy(device)
        rp.handle(lighting_request)

        analytics_repository.save_lighting_request(request)
        return "Success", 200

    except requests.HTTPError as e:
        return str(e), e.errno


@app.route("/lighting/request/scene", methods=["POST"])
def scene_request() -> Response:
    try:
        scene_request = SceneRequest(**request.get_json())
        scene = scene_repository.find_by_name(scene_request.name)

        for lighting_request in scene.requests:
            device = device_repository.find_by_id(lighting_request.target)

            rp = ReverseProxy(device)
            rp.handle(lighting_request)

        analytics_repository.save_scene_request(request)
        return "Success", 200

    except requests.HTTPError as e:
        return str(e), e.errno


""" Scene CRUD """


@ app.route("/lighting/scene", methods=["POST"])
def add_scene() -> Response:
    scene_repository.save(request)
    return request.to_json()


@ app.route("/lighting/scene", methods=["GET"])
def get_all_scenes() -> Response:
    all_scenes = scene_repository.find_all()
    return jsonify(all_scenes)


@ app.route("/lighting/scene", methods=["PUT"])
def update_scene() -> Response:
    updated_scene = scene_repository.update(request)
    if updated_scene:
        return Scene(**updated_scene).to_json()
    else:
        abort(404, "Scene not found")


@ app.route("/lighting/scene/<string:id>", methods=["DELETE"])
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
