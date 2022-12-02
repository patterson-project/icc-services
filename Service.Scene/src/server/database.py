import os
import motor.motor_asyncio
from fastapi import HTTPException
from icc.models import SceneDto, SceneModel, PydanticObjectId, Device, SceneRequestRecord


class SceneRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin")
        self.scenes: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.scenes

    async def insert(self, scene: SceneDto) -> None:
        await self.scenes.insert_one(scene.to_bson())

    async def find_all(self) -> list[SceneModel]:
        cursor: motor.motor_asyncio.AsyncIOMotorCursor = self.scenes.find()
        return [SceneModel(**scene) for scene in await cursor.to_list(None)]

    async def find_by_name(self, name: str) -> SceneModel:
        scene = await self.scenes.find_one({"name": name})
        if scene is None:
            raise HTTPException(status_code=404, detail="Scene not found")
        return SceneModel(**scene)

    async def update(self, id: PydanticObjectId, scene: SceneDto) -> SceneModel:
        return SceneModel(**(await self.scenes.find_one_and_replace({"_id": id}, scene.to_bson())))

    async def delete(self, id: PydanticObjectId) -> SceneModel:
        return SceneModel(**(await self.scenes.find_one_and_delete({"_id": id})))


class DeviceRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin")
        self.devices: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.devices

    async def find_by_id(self, id: PydanticObjectId) -> Device:
        return Device(**(await self.devices.find_one({"_id": id})))


class AnalyticsRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin")
        self.scene_analytics: motor.motor_asyncio.AsyncIOMotorCollection = self.db.analytics.scenes

    async def insert(self, scene_request: SceneRequestRecord):
        self.scene_analytics.insert_one(scene_request.to_bson())
