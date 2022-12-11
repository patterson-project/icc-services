from fastapi import APIRouter
from server.database import AnalyticsRepository, DeviceRepository
from icc.models import PowerRequestDto, DeviceControllerProxy, PowerRequestRecord
from datetime import datetime
from httpx import AsyncClient

router = APIRouter()
analytics_repository = AnalyticsRepository()
device_repository = DeviceRepository()
http_client = AsyncClient()


@router.post(
    "",
    summary="Create a power request",
    response_description="The created power request",
)
async def create_power_request(power_request: PowerRequestDto):
    device = await device_repository.find_by_id(power_request.target_id)

    await http_client.post(
        DeviceControllerProxy.device_model_to_url.get(
            device.model) + "/request",
        json=power_request.to_json(),
    )

    request_record = PowerRequestRecord(
        time=datetime.utcnow().isoformat(), **power_request.__dict__
    )
    await analytics_repository.insert(request_record)

    return power_request.to_json()
