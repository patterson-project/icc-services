from device import Device
from config import Config
import requests


def update_controllers(device: Device):
    requests.put(
        Config.UrlGivenModel[device.model] + "/update"
    )
