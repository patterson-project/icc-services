from flask import Request
from config import Config
from device import Device, LightingDeviceTypes
from lightingrequest import LightingRequest
import requests


class ReverseProxy:
    def __init__(self, device: Device):
        self.device = device
        self.proxy = {
            LightingDeviceTypes.KasaBulb: self.kasa_bulb_request,
            LightingDeviceTypes.CustomLedStrip: self.custom_led_strip_request,
            LightingDeviceTypes.KasaLedStrip: self.kasa_led_strip_request,
        }

    def handle(self, request: Request):
        self.proxy[self.device.model](request)

    def kasa_bulb_request(self, request: LightingRequest):
        requests.post(Config.BULB_CONTROLLER_URL +
                      "/request", json=request.to_json())

    def custom_led_strip_request(self, request: LightingRequest):
        requests.post(
            f"http://{self.device.ip}:8000/request", json=request.to_json())

    def kasa_led_strip_request(self, request: LightingRequest):
        requests.post(Config.LED_CONTROLLER_URL +
                      "/request", json=request.to_json())
