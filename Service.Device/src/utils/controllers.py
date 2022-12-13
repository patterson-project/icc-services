from httpx import AsyncClient
from icc.models import DeviceControllerProxy


async def update_controller(device_model: str) -> None:
    http_client = AsyncClient()
    await http_client.post(DeviceControllerProxy.device_model_to_url.get(
        device_model) + "/update")
