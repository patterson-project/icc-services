from lightingrequest import LightingRequest
from pymongo.collection import Collection
from flask import Request


def insert_lighting_request(lighting_request_db: Collection, request: Request):
    lighting_request = LightingRequest(**request.get_json())
    lighting_request_db.insert_one(lighting_request.to_bson())
