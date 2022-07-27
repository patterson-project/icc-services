from pymongo import MongoClient

mongo_client = MongoClient(
    f"mongodb://{input('Username: ')}:{input('Password: ')}@{input('Database IP: ')}:27017/iot?authSource=admin"
)

# Creating unique name field constraint for devices
device_db = mongo_client.iot.devices
device_db.create_index([("name", 1), ("ip", 1)])
