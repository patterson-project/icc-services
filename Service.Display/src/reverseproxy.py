from icc.models import ChromecastRequest
from config import Config
import requests


class ReverseProxy:
    def media_request(self, request: ChromecastRequest) -> requests.Response:
        return requests.post(Config.CHROMECAST_CONTROLLER_URL +
                             "/request/media", json=request.to_json())

    def get_media(self) -> requests.Response:
        return requests.get(Config.CHROMECAST_CONTROLLER_URL +
                            "/media")
