from fastapi import APIRouter
from server.database import DeviceRepository
from icc.models import PowerRequestDto, PydanticObjectId
from plug import Plug
from utils import initialize_plugs

router = APIRouter()
device_repository = DeviceRepository()

global plugs
plugs: dict[PydanticObjectId, Plug] = initialize_plugs(device_repository)


@router.post(
    "", summary="Create a plug request", response_description="The created plug request"
)
async def create_device(power_request: PowerRequestDto):
    plug: Plug = plugs[power_request.target_id]
    await plug.execute_request(power_request)
    return power_request.to_json()
