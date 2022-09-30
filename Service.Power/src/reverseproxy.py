from flask import Request
from config import Config
from device import Device, LightingDeviceTypes
from powerrequest import PowerRequest
import requests


class ReverseProxy:
    def __init__(self, device):
        self.proxy = {
            LightingDeviceTypes.KasaPlug: self.kasa_plug_request,
        }
        self.device: Device = device

    def handle(self, request: Request):
        self.proxy[self.device.model](request)

    def kasa_plug_request(self, request: PowerRequest):
        requests.post(Config.UrlGivenModel[self.device.model] +
                      "/request", json=request.to_json())
