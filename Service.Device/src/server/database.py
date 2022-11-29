import os
import motor.motor_asyncio
from fastapi import HTTPException
from icc.models import DeviceDto, DeviceModel, PydanticObjectId, RoomDto, RoomModel


class DeviceRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin")
        self.devices: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.devices
        self.rooms: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.rooms

    async def insert(self, device: DeviceDto) -> None:
        if await self.rooms.find({"_id": device.room}).count() == 0:
            raise HTTPException(status_code=404, detail="Room not found")
        else:
            await self.devices.insert_one(device.to_bson())

    async def find_by_id(self, id: PydanticObjectId) -> DeviceModel:
        return DeviceModel(**(await self.devices.find_one({"_id": id})))

    async def find_all(self) -> list[DeviceModel]:
        cursor: motor.motor_asyncio.AsyncIOMotorCursor = self.devices.find()
        return [DeviceModel(**device) for device in await cursor.to_list(None)]

    async def update(self, id: PydanticObjectId, device: DeviceDto) -> DeviceModel:
        return DeviceModel(**(await self.devices.find_one_and_replace({"_id": id}, device.to_bson())))

    async def delete(self, id: PydanticObjectId) -> DeviceModel:
        return DeviceModel(**(await self.devices.find_one_and_delete({"_id": id})))


class RoomRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin")
        self.rooms: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.rooms

    async def insert(self, room: RoomDto) -> None:
        await self.rooms.insert_one(room.to_bson())

    async def find_all(self) -> list[RoomModel]:
        print("IN FIND ALLLLLLLLLLLLLLl")
        cursor: motor.motor_asyncio.AsyncIOMotorCursor = self.rooms.find()
        return [RoomModel(**room) for room in await cursor.to_list(None)]

    async def update(self, id: PydanticObjectId, room: RoomDto) -> RoomModel:
        return RoomModel(**(await self.rooms.find_one_and_replace({"_id": id}, room.to_bson())))

    async def delete(self, id: PydanticObjectId) -> RoomModel:
        return RoomModel(**(await self.rooms.find_one_and_delete({"_id": id})))
