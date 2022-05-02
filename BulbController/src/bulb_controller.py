from contextlib import AsyncExitStack
from threading import Thread
from kasa import SmartBulb
from asyncio_mqtt import Client
from multiprocessing import Process
import asyncio
from utils import log, LightingRequest
from json import loads


class BulbController:
    BROKER_ADDRESS = "10.0.0.35"

    async def create_bulb(self, ip_address: str, topic: str) -> None:
        self.ip_address: str = ip_address
        self.topic: str = topic
        self.bulb: SmartBulb = await self.bulb_init()
        self.sequence_process: Process = None
        self.request: LightingRequest = None
        self.operation_callback_by_name = {
            "hsv": self.hsv,
            "brightness": self.brightness,
            "rainbow": self.rainbow,
        }

    async def bulb_init(self) -> SmartBulb:
        bulb = SmartBulb(self.ip_address)
        await bulb.update()
        return bulb

    async def cancel_tasks(tasks) -> None:
        for task in tasks:
            if task.done():
                continue
            try:
                task.cancel()
                await task
            except asyncio.CancelledError:
                pass

    async def async_mqtt(self) -> Client:
        async with AsyncExitStack() as stack:
            tasks = set()
            stack.push_async_callback(self.cancel_tasks, tasks)

            client = Client(self.BROKER_ADDRESS)
            await stack.enter_async_context(client)

            manager = client.filtered_messages(f"home/lighting/{self.topic}")
            messages = await stack.enter_async_context(manager)
            task = asyncio.create_task(self.message_callbacks(messages))
            tasks.add(task)

            await client.subscribe(f"home/lighting/{self.topic}")
            await asyncio.gather(*tasks)

    async def message_callbacks(self, messages):
        async for message in messages:
            lighting_request = LightingRequest(**loads(message.payload))
            log(message.topic, str(lighting_request.__dict__))

            self.request = lighting_request
            await self.operation_callback_by_name[lighting_request.operation]()

    async def hsv(self):
        await self.bulb.set_hsv(self.request.h, self.request.s, self.request.v)
        await self.bulb.update()

    def brightness(self):
        pass

    def rainbow(self):
        pass


async def turn_off(bulb):
    await bulb.turn_off()


async def main():
    bulb_1 = BulbController()
    await bulb_1.create_bulb("10.0.0.86", "bulb-1")

    while True:
        await bulb_1.async_mqtt()


if __name__ == "__main__":
    asyncio.run(main())
