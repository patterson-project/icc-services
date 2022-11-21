from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from server.database import SceneRepository, DeviceRepository, AnalyticsRepository
from icc.models import SceneRequestDto, SceneModel, DeviceControllerProxy
from threading import Thread
from httpx import AsyncClient
import asyncio

router = APIRouter()
http_client = AsyncClient()

scene_repository = SceneRepository()
device_repository = DeviceRepository()
analytics_repository = AnalyticsRepository()


@router.post("", tags=["Scenes"], summary="Request a scene", response_description="Scene which was executed")
async def scene_request(scene_request: SceneRequestDto):
    scene: SceneModel = await scene_repository.find_by_name(scene_request.name)
    tasks = []

    for lighting_request in scene.lighting_requests:
        device = await device_repository.find_by_id(lighting_request.target_id)
        tasks.append(asyncio.create_task(http_client.post(DeviceControllerProxy.device_model_to_url.get(
            device.model), data=lighting_request.to_json())))

    for power_request in scene.power_requests:
        device = await device_repository.find_by_id(power_request.target_id)
        tasks.append(asyncio.create_task(http_client.post(DeviceControllerProxy.device_model_to_url.get(
            device.model), data=power_request.to_json())))

    await asyncio.gather(*tasks)
    await analytics_repository.insert_scene(scene_request)

    return jsonable_encoder(scene)
