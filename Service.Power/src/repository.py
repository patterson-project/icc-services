from powerrequest import PowerRequest
from pymongo.collection import Collection
from flask import Request


def insert_power_request(power_requests: Collection, request: Request):
    lighting_request = PowerRequest(**request.get_json())
    power_requests.insert_one(lighting_request.to_bson())
