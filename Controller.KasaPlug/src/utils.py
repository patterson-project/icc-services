import asyncio
from objectid import PydanticObjectId
from plug import Plug
from repository import DeviceRepository


def initialize_plugs(device_repository: DeviceRepository, loop: asyncio.AbstractEventLoop):
    kasa_plugs = device_repository.find_all_kasa_plugs()
    plugs: dict[PydanticObjectId, Plug] = {}

    for device in kasa_plugs:
        plug = Plug()
        asyncio.run_coroutine_threadsafe(
            plug.create_plug(device.ip), loop)
        plugs[device.id] = plug

    return plugs

def start_background_loop(loop: asyncio.AbstractEventLoop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
