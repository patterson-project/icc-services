import os
from flask import Flask, Request
from flask_pymongo import PyMongo
from pymongo.collection import Collection
from chromecastrequest import ChromecastRequest


class AnalyticsRepository:
    def __init__(self, app: Flask):
        self.analyticsdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
        self.chromecast_requests: Collection = self.analyticsdb.db.chromecast_requests

    def save_chromecast_request(self, request: Request):
        movie_request = ChromecastRequest(**request.get_json())
        self.chromecast_requests.insert_one(movie_request.to_bson())
