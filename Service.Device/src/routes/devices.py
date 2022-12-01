from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from server.database import DeviceRepository
from icc.models import DeviceDto, PydanticObjectId, DeviceControllerProxy
from httpx import AsyncClient

router = APIRouter()
device_repository = DeviceRepository()
http_client = AsyncClient()


async def update_controller(device_model: str) -> None:
    await http_client.post(DeviceControllerProxy.device_model_to_url.get(
        device_model) + "/update")


@router.post("", summary="Create a device", response_description="The created device")
async def create_device(device: DeviceDto):
    await device_repository.insert(device)
    await update_controller(device.model)
    return device.to_json()


@router.get("/{id}", summary="Get a device by ID", response_description="The device")
async def get_device(id: PydanticObjectId):
    device = await device_repository.find_by_id(id)
    return device.to_json()


@router.get("", summary="Get all devices", response_description="List of all devices")
async def get_all_devices():
    devices = await device_repository.find_all()
    return jsonable_encoder(devices)


@router.put("/{id}", summary="Update a device", response_description="Updated device object")
async def update_device(id: PydanticObjectId, device: DeviceDto):
    updated_device = await device_repository.update(id, device)
    await update_controller(device.model)
    return jsonable_encoder(updated_device)


@router.delete("/{id}", summary="Delete a device", response_description="Deleted device")
async def delete_device(id: PydanticObjectId):
    device = await device_repository.find_by_id(id)
    deleted_device = await device_repository.delete(id)
    await update_controller(device.model)
    return jsonable_encoder(deleted_device)
