import os
from showrequest import ShowRequest
from movierequest import MovieRequest
from flask import Flask, Request
from flask_pymongo import PyMongo
from pymongo.collection import Collection


class AnalyticsRepository:
    def __init__(self, app: Flask):
        self.analyticsdb = PyMongo(
            app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/analytics?authSource=admin")
        self.movie_requests: Collection = self.analyticsdb.db.movie_requests
        self.show_requests: Collection = self.analyticsdb.db.show_requests

    def save_movie_request(self, request: Request):
        movie_request = MovieRequest(**request.get_json())
        self.movie_requests.insert_one(movie_request.to_bson())

    def save_show_request(self, request: Request):
        show_request = ShowRequest(**request.get_json())
        self.show_requests.insert_one(show_request.to_bson())
