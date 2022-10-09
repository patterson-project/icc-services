from showrequest import ShowRequest
from movierequest import MovieRequest
from config import Config
import requests


class ReverseProxy:
    def chromecast_movie_request(self, request: MovieRequest):
        requests.post(Config.CHROMECAST_CONTROLLER_URL +
                      "/request/movie", json=request.to_json())

    def chromecast_show_request(self, request: ShowRequest):
        requests.post(Config.CHROMECAST_CONTROLLER_URL +
                      "/request/show", json=request.to_json())
