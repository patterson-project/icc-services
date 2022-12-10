import os
import motor.motor_asyncio
from fastapi import HTTPException
from icc.models import DeviceDto, DeviceModel, PydanticObjectId


class DeviceRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin"
        )
        self.devices: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.devices

    async def find_all_kasa_plugs(self) -> list[DeviceModel]:
        cursor: motor.motor_asyncio.AsyncIOMotorCursor = self.devices.find(
            {"type": "Power", "model": "Kasa Plug"}
        )
        return [DeviceModel(**device) for device in await cursor.to_list(None)]
