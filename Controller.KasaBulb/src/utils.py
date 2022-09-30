import asyncio
from objectid import PydanticObjectId
from bulb import Bulb
from repository import DeviceRepository


def initialize_bulbs(device_repository: DeviceRepository, loop: asyncio.AbstractEventLoop):
    kasa_bulbs = device_repository.find_all_kasa_bulbs()
    bulbs: dict[PydanticObjectId, Bulb] = {}

    for bulb_device in kasa_bulbs:
        bulb = Bulb()
        asyncio.run_coroutine_threadsafe(
            bulb.create_bulb(bulb_device.ip), loop)
        bulbs[bulb_device.id] = bulb

    return bulbs


def start_background_loop(loop: asyncio.AbstractEventLoop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
