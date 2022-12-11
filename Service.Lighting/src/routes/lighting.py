from fastapi import APIRouter
from server.database import AnalyticsRepository, DeviceRepository
from icc.models import LightingRequestDto, DeviceControllerProxy, LightingRequestRecord
from datetime import datetime
from httpx import AsyncClient

router = APIRouter()
analytics_repository = AnalyticsRepository()
device_repository = DeviceRepository()
http_client = AsyncClient()


@router.post(
    "",
    summary="Create a lighting request",
    response_description="The created lighting request",
)
async def create_lighting_request(lighting_request: LightingRequestDto):
    device = await device_repository.find_by_id(lighting_request.target_id)

    await http_client.post(
        DeviceControllerProxy.device_model_to_url.get(
            device.model) + "/request",
        json=lighting_request.to_json(),
    )

    request_record = LightingRequestRecord(
        time=datetime.utcnow().isoformat(), **lighting_request.__dict__
    )
    await analytics_repository.insert(request_record)

    return lighting_request.to_json()
