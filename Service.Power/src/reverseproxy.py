import requests
from flask import Request
from config import Config
from icc.models import PowerDeviceTypes, PowerRequest, Device


class ReverseProxy:
    def __init__(self, device):
        self.proxy = {
            PowerDeviceTypes.KasaPlug: self.kasa_plug_request,
        }
        self.device: Device = device

    def handle(self, request: Request) -> requests.Response:
        return self.proxy[self.device.model](request)

    def kasa_plug_request(self, request: PowerRequest) -> requests.Response:
        return requests.post(Config.UrlGivenModel[self.device.model] +
                             "/request", json=request.to_json())
