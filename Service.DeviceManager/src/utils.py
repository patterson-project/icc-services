from device import Device
from config import Config
import requests


def update_bulb_controller(device: Device):
    if device.model == "Kasa Bulb":
        requests.put(
            Config.BULB_CONTROLLER_URL
        )
