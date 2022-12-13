from fastapi import APIRouter, Response
from server.database import DeviceRepository
from icc.models import LightingRequestDto, PydanticObjectId, DeviceModel
from utils.ledstrip import LedStrip

router = APIRouter()
device_repository = DeviceRepository()

strips: dict[PydanticObjectId, LedStrip] = {}


@router.on_event("startup")
async def initialize_strips():
    kasa_led_strips: list[DeviceModel] = await device_repository.find_all_kasa_led_strips()

    global strips
    for device in kasa_led_strips:
        strip = LedStrip()
        await strip.create_strip(device.ip)
        strips[device.id] = strip


@router.post(
    path="/request", summary="Create a Kasa Led Strip lighting request", response_description="The created lighting request"
)
async def create_power_request(lighting_request: LightingRequestDto):
    strip: LedStrip = strips[lighting_request.target_id]
    await strip.execute_request(lighting_request)
    return lighting_request.to_json()


@router.post(
    path="/update", summary="Update & reinitialize Kasa Led Strip controllers", response_description="Success message"
)
async def update_plugs():
    global strips
    strips = await initialize_strips()
    return Response(status_code=200)
