from chromecastrequest import ChromecastRequest
from config import Config
import requests


class ReverseProxy:
    def cast_request(self, request: ChromecastRequest) -> requests.Response:
        return requests.post(Config.CHROMECAST_CONTROLLER_URL +
                             "/request/cast", json=request.to_json())
