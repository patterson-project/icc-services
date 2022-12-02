import os
import motor.motor_asyncio
from fastapi import HTTPException
from icc.models import LightingRequestRecord, DeviceDto, DeviceModel, PydanticObjectId


class DeviceRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin")
        self.devices: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.devices

    async def insert(self, device: DeviceDto) -> None:
        await self.devices.insert_one(device.to_bson())

    async def find_by_id(self, id: PydanticObjectId) -> DeviceModel:
        device = await self.devices.find_one({"_id": id})
        if device is None:
            raise HTTPException(status_code=404, detail="Device not found")
        return DeviceModel(**(device))


class AnalyticsRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin")
        self.lighting_analytics: motor.motor_asyncio.AsyncIOMotorCollection = self.db.analytics.lighting

    async def insert(self, lighting_request: LightingRequestRecord) -> None:
        await self.lighting_analytics.insert_one(lighting_request.to_bson())
