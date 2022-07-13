from flask import Flask, Response, Request, request, url_for, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from gevent.pywsgi import WSGIServer
from pymongo.collection import Collection, ReturnDocument
from pymongo.errors import DuplicateKeyError
from model import Device

app = Flask("__main__")
CORS(app)
pymongo = PyMongo(app)

devices: Collection = pymongo.db.devices


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(DuplicateKeyError)
def resource_not_found(e):
    return jsonify(error=f"Duplicate key error."), 400


@app.route("/devices", methods=["POST"])
def new_device():
    raw_device = request.get_json()
    device = Device(**raw_device)
    devices.insert_one(device)
    return device.to_json()


if __name__ == "__main__":
    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
