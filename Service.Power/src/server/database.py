import os
import motor.motor_asyncio
from fastapi import HTTPException
from icc.models import PowerRequestDto, DeviceModel, PydanticObjectId


class DeviceRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin"
        )
        self.devices: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.devices

    async def find_by_id(self, id: PydanticObjectId) -> DeviceModel:
        device = await self.devices.find_one({"_id": id})
        if device is None:
            raise HTTPException(status_code=404, detail="Device not found")
        return DeviceModel(**(device))


class AnalyticsRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin"
        )
        self.power_analytics: motor.motor_asyncio.AsyncIOMotorCollection = (
            self.db.analytics.power
        )

    async def insert(self, power_request: PowerRequestDto) -> None:
        await self.power_analytics.insert_one(power_request.to_bson())
