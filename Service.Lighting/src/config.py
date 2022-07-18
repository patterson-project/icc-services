import datetime
import os
from pymongo import MongoClient
from flask import Request


class ServiceUris:
    MONGO_DB_URI = f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin"
    LED_STRIP_SERVICE = "http://10.0.0.63:8000"
    BULB_CONTROLLER = "controller.bulb:8000"
