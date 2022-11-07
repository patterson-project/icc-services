import os
from typing import Any
from pymongo import ReturnDocument
from flask import Flask, Request
from flask_pymongo import PyMongo
from pymongo.results import InsertOneResult
from pymongo.collection import Collection
from icc.models import Device, PydanticObjectId, State


class DeviceRepository:
    def __init__(self, app: Flask):
        self.iotdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
        self.devices: Collection = self.iotdb.db.devices

    def save(self, request: Request) -> InsertOneResult:
        device = Device(**request.get_json())
        return self.devices.insert_one(device.to_bson())

    def update(self, request: Request) -> Any:
        device = Device(**request.get_json())
        return self.devices.find_one_and_update(
            {"_id": device.id},
            {"$set": device.to_bson()},
            return_document=ReturnDocument.AFTER,
        )

    def find_all(self) -> list[Any]:
        return list(Device(**device).to_json() for device in self.devices.find())

    def delete(self, id: str) -> Any:
        return self.devices.find_one_and_delete({"_id": PydanticObjectId(id)})


class StateRepository:
    def __init__(self, app: Flask):
        self.iotdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
        self.states: Collection = self.iotdb.db.states

    def save(self, device: PydanticObjectId, state: bool) -> None:
        self.states.insert_one({"device": device, "state": state})

    def update(self, device: PydanticObjectId, state: bool) -> None:
        self.states.find_one_and_update({"device": device}, {
            "$set": {"state": state}}, upsert=True)

    def find_all(self) -> list[Any]:
        return list(State(**state).to_json() for state in self.states.find())

    def delete(self, id: str) -> None:
        self.states.find_one_and_delete({"device": PydanticObjectId(id)})
