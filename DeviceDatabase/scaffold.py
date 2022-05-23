import os
from pymongo import MongoClient

from device import Device

client = MongoClient(
    f'mongodb://{os.environ["MONGO_DB_USERNAME"]}:{os.environ["MONGO_DB_PASSWORD"]}@localhost:27017'
)

devicesdb = client["iot-devices"]

states = devicesdb["states"]
devices = devicesdb["devices"]
requests = devicesdb["requests"]

led_strip = Device("WS-2811 LED Strip", "lighting")
kasa_bulb_1 = Device("TP-Link Kasa Smart-Bulb (1)", "lighting")
kasa_bulb_2 = Device("TP-Link Kasa Smart-Bulb (2)", "lighting")

devices.insert_many([led_strip.__dict__, kasa_bulb_1.__dict__, kasa_bulb_2.__dict__])
