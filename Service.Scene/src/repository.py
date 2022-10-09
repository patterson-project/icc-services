import os
from typing import Any
from pymongo import ReturnDocument
from device import Device
from objectid import PydanticObjectId
from lightingrequest import LightingRequest
from flask import Flask, Request
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from scene import Scene, SceneDto


class SceneRepository:
    def __init__(self, app: Flask):
        self.iotdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
        self.scenes: Collection = self.iotdb.db.scenes

    def save(self, request: Request) -> None:
        scene_request = SceneDto(**request.get_json())
        self.scenes.insert_one(scene_request.to_bson())

    def find_by_name(self, name: str) -> Scene:
        return Scene(**self.scenes.find_one({"name": name}))

    def find_all(self) -> list:
        return list(Scene(**scene).to_json()
                    for scene in self.scenes.find())

    def update(self, request: Request) -> Any:
        scene = Scene(**request.get_json())
        return self.scenes.find_one_and_update(
            {"_id": scene.id},
            {"$set": scene.to_bson()},
            return_document=ReturnDocument.AFTER,
        )

    def delete(self, id: PydanticObjectId):
        return self.scenes.find_one_and_delete({"_id": id})


class DeviceRepository:
    def __init__(self, app: Flask):
        self.iotdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
        self.devices: Collection = self.iotdb.db.devices

    def find_by_id(self, id: PydanticObjectId) -> Device:
        return Device(**self.devices.find_one({"_id": id}))


class AnalyticsRepository:
    def __init__(self, app: Flask):
        self.analyticsdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
        self.lighting_requests: Collection = self.analyticsdb.db.lighting_requests
        self.scene_requests: Collection = self.analyticsdb.db.scene_requests

    def save_scene_request(self, request: Request):
        scene_request = SceneDto(**request.get_json())
        self.scene_requests.insert_one(scene_request.to_bson())
