from flask import Flask
import pychromecast
from chromecastplayer import ChromecastPlayer
from objectid import PydanticObjectId
from repository import DeviceRepository


def initialize_chromecasts(device_repository: DeviceRepository) -> dict[PydanticObjectId, ChromecastPlayer]:
    chromecast_devices = device_repository.find_all_chromecasts()
    chromecasts: dict[PydanticObjectId, ChromecastPlayer] = {}
    network_chromecasts: list[pychromecast.Chromecast] = pychromecast.get_chromecasts()[
        0]

    for chromecast_device in chromecast_devices:
        chromecast_player = next(
            (cc for cc in network_chromecasts if cc.cast_info.host == chromecast_device.ip), None)

        if chromecast_player is not None:
            chromecasts[chromecast_device.id] = ChromecastPlayer(
                chromecast_player)

    return chromecasts
