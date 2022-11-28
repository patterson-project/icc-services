import os
import motor.motor_asyncio
from icc.models import DeviceDto, DeviceModel, PydanticObjectId


class DeviceRepository:
    def __init__(self):
        self.db: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(
            f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/?authSource=admin")
        self.devices: motor.motor_asyncio.AsyncIOMotorCollection = self.db.iot.devices

    async def insert(self, device: DeviceDto) -> None:
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

# TODO: State management

# class StateRepository:
#     def __init__(self, app: Flask):
#         self.iotdb = PyMongo(
#             app, uri=f"mongodb://{os.getenv('MONGO_DB_USERNAME')}:{os.getenv('MONGO_DB_PASSWORD')}@{os.getenv('MONGO_DB_IP')}:27017/iot?authSource=admin")
#         self.states: Collection = self.iotdb.db.states

#     def save(self, device: PydanticObjectId, state: bool) -> None:
#         self.states.insert_one({"device": device, "state": state})

#     def update(self, device: PydanticObjectId, state: bool) -> None:
#         self.states.find_one_and_update({"device": device}, {
#             "$set": {"state": state}}, upsert=True)

#     def find_all(self) -> list[Any]:
#         return list(State(**state).to_json() for state in self.states.find())

#     def delete(self, id: str) -> None:
#         self.states.find_one_and_delete({"device": PydanticObjectId(id)})
