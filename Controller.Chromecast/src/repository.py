import os
from icc.models import Device
from flask import Flask
from flask_pymongo import PyMongo
from pymongo.collection import Collection


class DeviceRepository:
    def __init__(self, app: Flask):
        self.iotdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
        self.devices: Collection = self.iotdb.db.devices

    def find_all_chromecasts(self) -> list[Device]:
        return list(
            Device(**device)
            for device in self.devices.find({"type": "Display", "model": "Chromecast"})
        )
