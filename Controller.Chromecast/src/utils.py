from flask import Flask
import pychromecast
from chromecastplayer import ChromecastPlayer
from objectid import PydanticObjectId
from repository import DeviceRepository


def initialize_chromecasts(device_repository: DeviceRepository) -> dict[PydanticObjectId, ChromecastPlayer]:
    chromecast_devices = device_repository.find_all_chromecasts()
    chromecasts: dict[PydanticObjectId, ChromecastPlayer] = {}

    for chromecast_device in chromecast_devices:
        chromecast_player = pychromecast.get_chromecast_from_host(
            chromecast_device.ip)
        chromecasts[chromecast_device.id] = ChromecastPlayer(
            chromecast_player)
        print(f"{chromecast_player.cast_info.host} initialized")

    return chromecasts


app = Flask("__main__")
dp = DeviceRepository(app)
initialize_chromecasts(dp)
