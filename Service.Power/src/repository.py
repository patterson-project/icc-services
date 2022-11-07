import os
from flask import Flask, Request
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from icc.models import Device, PydanticObjectId, PowerRequest

class DeviceRepository:
    def __init__(self, app: Flask):
        self.iotdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
        self.devices: Collection = self.iotdb.db.devices

    def find_by_id(self, id: PydanticObjectId) -> Device:
        return Device(**self.devices.find_one({"_id": id}))

    def find_by_name(self, name: str) -> Device:
        return Device(**self.devices.find_one({"name": name}))


class AnalyticsRepository:
    def __init__(self, app: Flask):
        self.analyticsdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
        self.lighting_requests: Collection = self.analyticsdb.db.lighting_requests
        self.scene_requests: Collection = self.analyticsdb.db.scene_requests

    def save_power_request(self, request: Request):
        lighting_request = PowerRequest(**request.get_json())
        self.lighting_requests.insert_one(lighting_request.to_bson())

