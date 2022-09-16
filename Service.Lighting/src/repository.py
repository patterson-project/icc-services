from lightingrequest import LightingRequest
from scenerequest import SceneRequest
from pymongo.collection import Collection
from flask import Request


def insert_lighting_request(lighting_requests: Collection, request: Request):
    lighting_request = LightingRequest(**request.get_json())
    lighting_requests.insert_one(lighting_request.to_bson())


def insert_scene_request(scene_requests: Collection, request: Request):
    scene_request = SceneRequest(**request.get_json())
    scene_requests.insert_one(scene_request.to_bson())
