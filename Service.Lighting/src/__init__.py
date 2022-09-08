import os
import requests
from flask import Flask, Response, request, jsonify, abort
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import ObjectId
from gevent.pywsgi import WSGIServer
from pymongo.collection import Collection, ReturnDocument
from pymongo.errors import DuplicateKeyError
from repository import insert_lighting_request, insert_scene_request
from device import Device
from scenerequest import Scene, SceneRequest
from lightingrequest import LightingRequest
from reverseproxy import ReverseProxy


""" Flask and Pymongo Setup """


app: Flask = Flask("__main__")
CORS(app)

analyticsdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
lighting_requests: Collection = analyticsdb.db.lighting_requests
scene_requests: Collection = analyticsdb.db.scene_requests

iotdb = PyMongo(
    app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
devices: Collection = iotdb.db.devices
scenes: Collection = iotdb.db.scenes


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
        device = Device(**devices.find_one({"_id": lighting_request.target}))

        rp = ReverseProxy(device)
        rp.handle(lighting_request)

        insert_lighting_request(lighting_requests, request)

        return "Success", 200

    except requests.HTTPError as e:
        return str(e), e.errno


@app.route("/lighting/request/name", methods=["POST"])
def name_request() -> Response:
    try:
        lighting_request = LightingRequest(**request.get_json())
        device = Device(**devices.find_one({"name": lighting_request.name}))
        lighting_request.target = device.id

        rp = ReverseProxy(device)
        rp.handle(lighting_request)

        insert_lighting_request(lighting_requests, request)

        return "Success", 200

    except requests.HTTPError as e:
        return str(e), e.errno


@app.route("/lighting/request/scene", methods=["POST"])
def scene_request() -> Response:
    try:
        scene_request = SceneRequest(**request.get_json())
        scene = Scene(**scenes.find_one({"name": scene_request.name}))

        for lighting_request in scene.requests:
            device = Device(
                **devices.find_one({"name": lighting_request.name}))

            rp = ReverseProxy(device)
            rp.handle(lighting_request)

        insert_scene_request(scene_requests, request)

    except requests.HTTPError as e:
        return str(e), e.errno


""" Scene CRUD """


@app.route("/lighting/scene", methods=["POST"])
def add_scene() -> Response:
    scene = Scene(**request.get_json())
    scenes.insert_one(scene.to_bson())

    return scene.to_json()


@app.route("/lighting/scene", methods=["GET"])
def get_all_scenes() -> Response:
    all_scenes = list(Scene(**scene).to_json()
                      for scene in scenes.find())
    return jsonify(all_scenes)


@app.route("/lighting/scene", methods=["PUT"])
def update_scene() -> Response:
    scene = Scene(**request.get_json())
    updated_scene = scenes.find_one_and_update(
        {"_id": scene.id},
        {"$set": scene.to_bson()},
        return_document=ReturnDocument.AFTER,
    )
    if updated_scene:
        return Scene(**updated_scene).to_json()
    else:
        abort(404, "Scene not found")


@app.route("/lighting/scene/<string:id>", methods=["DELETE"])
def delete_device(id: str) -> Response:
    deleted_scene = scenes.find_one_and_delete({"_id": ObjectId(id)})
    if deleted_scene:
        scene = Scene(**deleted_scene)
        return scene.to_json()
    else:
        abort(404, "Scene not found")


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
