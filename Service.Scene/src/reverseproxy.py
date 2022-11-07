from flask import Request
from config import Config
from icc.models import LightingDeviceTypes, PowerDeviceTypes, LightingRequest, Device, PowerRequest
import requests


class ReverseProxy:
    def __init__(self, device):
        self.proxy = {
            LightingDeviceTypes.KasaBulb: self.lighting_request,
            LightingDeviceTypes.CustomLedStrip: self.lighting_request,
            LightingDeviceTypes.KasaLedStrip: self.lighting_request,
            PowerDeviceTypes.KasaPlug: self.power_request
        }
        self.device: Device = device

    def handle(self, request: Request):
        return self.proxy[self.device.model](request)

    def lighting_request(self, request: LightingRequest) -> requests.Response:
        return requests.post(Config.LIGHTING_SERVICE_URL +
                             "/request", json=request.to_json())

    def power_request(self, request: PowerRequest) -> requests.Response:
        return requests.post(Config.POWER_SERVICE_URL +
                             "/request", json=request.to_json())
