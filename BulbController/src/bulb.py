import asyncio
import time
import os
import kasa
from utils import LightingRequest
from pymongo import MongoClient


class BulbController:
    async def create_bulb(self, ip_address: str) -> None:
        self.ip_address: str = ip_address
        self.bulb: kasa.SmartBulb = None
        await self.bulb_init()
        self.sequence_task: asyncio.Task = None
        self.request: LightingRequest = None
        self.operation_callback_by_name = {
            "on": self.on,
            "off": self.off,
            "hsv": self.hsv,
            "brightness": self.brightness,
            "scene": self.scene,
            "rainbow": self.rainbow,
            "rainbow_cycle": self.rainbow,
            "temperature": self.temperature,
        }
        print("Bulb controller initialization completed successfully.")

    async def bulb_init(self) -> kasa.SmartBulb:
        try:
            self.bulb = kasa.SmartBulb(self.ip_address)
            await (self.bulb.update())
        except kasa.SmartDeviceException:
            print("SmartDeviceException: Unable to establish connection with device.")

    def set_request(self, request: LightingRequest) -> None:
        self.request = request

    def terminate_task(self) -> None:
        if self.sequence_task is not None:
            self.sequence_task.cancel()
            self.sequence_task = None

    async def update_bulb(self):
        await self.bulb.update()
        return True

    async def on(self):
        self.terminate_task()
        await self.bulb.turn_on()

    async def off(self):
        self.terminate_task()
        await self.bulb.turn_off()

    async def hsv(self):
        self.terminate_task()
        await self.bulb.set_hsv(
            int(self.request.h), int(self.request.s), int(self.request.v)
        )

    async def scene(self):
        self.terminate_task()
        color = self.request.scene
        if color == "ocean":
            await self.bulb.set_hsv(245, 84, 100)
        if color == "rose":
            await self.bulb.set_hsv(304, 56, 100)

    async def brightness(self):
        if self.sequence_task is None:
            await self.bulb.set_brightness(self.request.brightness)
        else:
            last_sequence = self.sequence_task.get_name()
            self.terminate_task()
            await self.bulb.set_brightness(self.request.brightness)
            await self.operation_callback_by_name[last_sequence]()

    async def temperature(self):
        self.terminate_task()
        await self.bulb.set_color_temp(int(self.request.temperature))

    async def rainbow(self):
        self.terminate_task()
        self.sequence_task = asyncio.create_task(self.rainbow_loop())
        self.sequence_task.set_name("rainbow")

    async def rainbow_loop(self):
        while True:
            for i in range(359):
                await self.bulb.set_hsv(i, 100, 100)
                time.sleep(0.05)
