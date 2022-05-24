import os
from state import State
from pymongo import MongoClient

from device import Device

client = MongoClient(
    f'mongodb://{os.environ["MONGO_DB_USERNAME"]}:{os.environ["MONGO_DB_PASSWORD"]}@localhost:27017'
)

iotdb = client["iot-devices"]

states = iotdb["states"]
devices = iotdb["devices"]

device_names = [
    "ledstrip",
    "bulb1",
    "bulb2",
]

device_descriptions = [
    "WS-2811 LED Strip",
    "TP-Link Kasa Smart-Bulb KL125",
    "TP-Link Kasa Smart-Bulb KL125",
]

lighting_devices = [
    Device(x, y, "lighting").__dict__ for x, y in zip(device_names, device_descriptions)
]
lighting_states = [State(x, False).__dict__ for x in device_names]

devices.insert_many(lighting_devices)
states.insert_many(lighting_states)
