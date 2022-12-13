from fastapi import APIRouter, Response
from server.database import DeviceRepository
from icc.models import PowerRequestDto, PydanticObjectId, DeviceModel
from utils.plug import Plug

router = APIRouter()
device_repository = DeviceRepository()

plugs: dict[PydanticObjectId, Plug] = {}


@router.on_event("startup")
async def initialize_plugs():
    kasa_plugs: list[DeviceModel] = await device_repository.find_all_kasa_plugs()

    for device in kasa_plugs:
        plug = Plug()
        await plug.create_plug(device.ip)
        global plugs
        plugs[device.id] = plug


@router.post(
    path="/request", summary="Create a plug request", response_description="The created plug request"
)
async def create_power_request(power_request: PowerRequestDto):
    plug: Plug = plugs[power_request.target_id]
    await plug.execute_request(power_request)
    return power_request.to_json()


@router.post(
    path="/update", summary="Update & reinitialize Kasa plug controllers", response_description="Success message"
)
async def update_plugs():
    global plugs
    plugs = await initialize_plugs()
    return Response(status_code=200)
