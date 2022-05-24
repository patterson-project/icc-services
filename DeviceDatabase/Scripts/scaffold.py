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
    "WS-2811 LED Strip",
    "TP-Link Kasa Smart-Bulb (1)",
    "TP-Link Kasa Smart-Bulb (2)",
]

led_strip_state = State()

lighting_devices = [Device(x, "lighting").__dict__ for x in device_names]
lighting_states = [State(x, False).__dict__ for x in device_names]

devices.insert_many(lighting_devices)
states.insert_many(lighting_states)
