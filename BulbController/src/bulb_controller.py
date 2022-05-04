import asyncio
from asyncio_mqtt import Client
from contextlib import AsyncExitStack
from json import loads
from kasa import SmartBulb, SmartDeviceException
from utils import log, BulbRequest


class BulbController:
    BROKER_ADDRESS = "10.0.0.35"

    async def create_bulb(self, ip_address: str, topic: str) -> None:
        self.ip_address: str = ip_address
        self.topic: str = topic
        self.bulb: SmartBulb = await self.bulb_init()
        self.sequence_task: asyncio.Task = None
        self.request: BulbRequest = None
        self.operation_callback_by_name = {
            "off": self.off,
            "hsv": self.hsv,
            "brightness": self.brightness,
            "rainbow": self.rainbow,
            "rainbow_cycle": self.rainbow,
        }

    async def bulb_init(self) -> SmartBulb:
        bulb = SmartBulb(self.ip_address)
        await bulb.update()
        return bulb

    def terminate_task(self) -> None:
        if self.sequence_task is not None:
            self.sequence_task.cancel()
            self.sequence_task = None

    async def async_mqtt(self) -> Client:
        async with AsyncExitStack() as stack:
            tasks = set()

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
            await self.bulb.update()
            lighting_request = BulbRequest(**loads(message.payload))
            log(message.topic, str(lighting_request.__dict__))

            self.request = lighting_request
            await self.operation_callback_by_name[lighting_request.operation]()

    async def off(self):
        self.terminate_task()
        await self.bulb.turn_off()

    async def hsv(self):
        self.terminate_task()
        await self.bulb.set_hsv(
            int(self.request.h), int(self.request.s), int(self.request.v)
        )
        await self.bulb.update()

    async def brightness(self):
        if self.sequence_task is None:
            await self.bulb.set_brightness(self.request.brightness)
            await self.bulb.update()
        else:
            last_sequence = self.sequence_task.get_name()
            self.terminate_task()
            await self.bulb.set_brightness(self.request.brightness)
            await self.bulb.update()
            await self.operation_callback_by_name[last_sequence]()

    async def rainbow(self):
        self.terminate_task()
        self.sequence_task = asyncio.create_task(self.rainbow_loop())
        self.sequence_task.set_name("rainbow")

    async def rainbow_loop(self):
        while True:
            for i in range(359):
                await self.bulb.set_hsv(i, 100, 100)
                await self.bulb.update()


async def main():
    bulb_1 = BulbController()
    await bulb_1.create_bulb("10.0.0.86", "bulb-1")
    print("Initialization completed successfully.")

    while True:
        try:
            await bulb_1.async_mqtt()
        except SmartDeviceException:
            bulb_1 = BulbController()
            await bulb_1.create_bulb("10.0.0.86", "bulb-1")


if __name__ == "__main__":
    asyncio.run(main())
