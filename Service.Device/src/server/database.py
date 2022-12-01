import os
import motor.motor_asyncio
from fastapi import HTTPException
from icc.models import DeviceDto, DeviceModel, PydanticObjectId


class DeviceRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin")
        self.devices: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.devices
        self.rooms: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.rooms

    async def insert(self, device: DeviceDto) -> None:
        await self.devices.insert_one(device.to_bson())

    async def find_by_id(self, id: PydanticObjectId) -> DeviceModel:
        device = await self.devices.find_one({"_id": id})
        if device is None:
            raise HTTPException(status_code=404, detail="Device not found")
        return DeviceModel(**(device))

    async def find_all(self) -> list[DeviceModel]:
        cursor: motor.motor_asyncio.AsyncIOMotorCursor = self.devices.find()
        return [DeviceModel(**device) for device in await cursor.to_list(None)]

    async def update(self, id: PydanticObjectId, device: DeviceDto) -> DeviceModel:
        device = await self.devices.find_one_and_replace({"_id": id}, device.to_bson())
        if device is None:
            raise HTTPException(status_code=404, detail="Device not found")
        return DeviceModel(**(device))

    async def delete(self, id: PydanticObjectId) -> DeviceModel:
        return DeviceModel(**(await self.devices.find_one_and_delete({"_id": id})))
