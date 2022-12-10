import asyncio
from icc.models import PydanticObjectId, DeviceModel
from plug import Plug
from server.database import DeviceRepository


async def initialize_plugs(device_repository: DeviceRepository):
    kasa_plugs: list[DeviceModel] = device_repository.find_all_kasa_plugs()
    plugs: dict[PydanticObjectId, Plug] = {}

    for device in kasa_plugs:
        plug = Plug()
        await plug.create_plug(device.ip)
        plugs[device.id] = plug

    return plugs
