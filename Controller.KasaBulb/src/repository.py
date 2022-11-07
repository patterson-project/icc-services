import os
from flask import Flask, Request
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from icc.models import Device, State, PydanticObjectId


class DeviceRepository:
    def __init__(self, app: Flask):
        self.iotdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
        self.devices: Collection = self.iotdb.db.devices

    def find_all_kasa_bulbs(self) -> list[Device]:
        return list(
            Device(**device)
            for device in self.devices.find({"type": "Lighting", "model": "Kasa Bulb"})
        )


class StateRepository:
    def __init__(self, app: Flask):
        self.iotdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
        self.states: Collection = self.iotdb.db.states

    def update(self, device: PydanticObjectId, state: bool):
        self.states.find_one_and_update({"device": device}, {
            "$set": {"state": state}}, upsert=True)


class AnalyticsRepository:
    def __init__(self, app: Flask):
        self.analyticsdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
        self.states: Collection = self.analyticsdb.db.states

    def save(self, device: PydanticObjectId, state: bool):
        self.states.insert_one(
            State(device=device, state=state).to_bson())
