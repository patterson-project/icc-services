import asyncio
from objectid import PydanticObjectId
from ledstrip import LedStrip
from repository import DeviceRepository


def initialize_led_strips(device_repository: DeviceRepository, loop: asyncio.AbstractEventLoop):
    kasa_led_strips = device_repository.find_all_kasa_led_strips()
    led_strips: dict[PydanticObjectId, LedStrip] = {}

    for device in kasa_led_strips:
        bulb = LedStrip()
        asyncio.run_coroutine_threadsafe(
            bulb.create_strip(device.ip), loop)
        led_strips[device.id] = bulb

    return led_strips

def start_background_loop(loop: asyncio.AbstractEventLoop):
    asyncio.set_event_loop(loop)
    loop.run_forever()