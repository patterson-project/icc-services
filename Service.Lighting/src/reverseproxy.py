from flask import Request
from config import Config
from icc.models import LightingRequest, Device, LightingDeviceTypes
import requests


class ReverseProxy:
    def __init__(self, device):
        self.proxy = {
            LightingDeviceTypes.KasaBulb: self.kasa_bulb_request,
            LightingDeviceTypes.CustomLedStrip: self.custom_led_strip_request,
            LightingDeviceTypes.KasaLedStrip: self.kasa_led_strip_request,
        }
        self.device: Device = device

    def handle(self, request: Request) -> requests.Response:
        return self.proxy[self.device.model](request)

    def kasa_bulb_request(self, request: LightingRequest) -> requests.Response:
        return requests.post(Config.BULB_CONTROLLER_URL +
                             "/request", json=request.to_json())

    def custom_led_strip_request(self, request: LightingRequest) -> requests.Response:
        return requests.post(
            f"http://{self.device.ip}:8000/request", json=request.to_json())

    def kasa_led_strip_request(self, request: LightingRequest) -> requests.Response:
        return requests.post(Config.LED_CONTROLLER_URL +
                             "/request", json=request.to_json())
