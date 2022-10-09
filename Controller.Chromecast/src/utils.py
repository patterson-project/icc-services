import asyncio
from chromecastplayer import ChromecastPlayer
from objectid import PydanticObjectId
from repository import DeviceRepository


def initialize_chromecasts(device_repository: DeviceRepository) -> dict[PydanticObjectId, ChromecastPlayer]:
    chromecast_devices = device_repository.find_all_chromecasts()
    chromecasts: dict[PydanticObjectId, ChromecastPlayer] = {}

    for chromecast in chromecast_devices:
        chromecasts[chromecast.id] = ChromecastPlayer(chromecast.ip)
        print(f"{chromecast.ip} initialized")

    return chromecasts


def start_background_loop(loop: asyncio.AbstractEventLoop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
