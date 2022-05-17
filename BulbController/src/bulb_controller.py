import asyncio
import os
import time
import asyncio_mqtt
import contextlib
import json
import kasa
from utils import log, BulbRequest


class BulbController:
    async def create_bulb(self, ip_address: str, topic: str) -> None:
        self.ip_address: str = ip_address
        self.topic: str = topic
        self.bulb: kasa.SmartBulb = None
        await self.bulb_init()
        self.sequence_task: asyncio.Task = None
        self.request: BulbRequest = None
        self.operation_callback_by_name = {
            "on": self.on,
            "off": self.off,
            "hsv": self.hsv,
            "brightness": self.brightness,
            "rainbow": self.rainbow,
            "rainbow_cycle": self.rainbow,
            "temperature": self.temperature,
        }

    async def bulb_init(self) -> kasa.SmartBulb:
        try:
            self.bulb = kasa.SmartBulb(self.ip_address)
            await self.bulb.update()
        except kasa.SmartDeviceException:
            log("SmartDeviceException: Unable to establish connection with device.")

    def terminate_task(self) -> None:
        if self.sequence_task is not None:
            self.sequence_task.cancel()
            self.sequence_task = None

    async def async_mqtt(self) -> asyncio_mqtt.Client:
        async with contextlib.AsyncExitStack() as stack:
            tasks = set()

            client = asyncio_mqtt.Client(
                hostname=os.environ["BROKER_IP"], port=int(os.environ["BROKER_PORT"])
            )
            await stack.enter_async_context(client)

            manager = client.filtered_messages(f"home/lighting/{self.topic}")
            messages = await stack.enter_async_context(manager)
            task = asyncio.create_task(self.message_callbacks(messages))
            tasks.add(task)

            await client.subscribe(f"home/lighting/{self.topic}")
            await asyncio.gather(*tasks)

    async def message_callbacks(self, messages):
        async for message in messages:
            lighting_request = BulbRequest(**json.loads(message.payload))
            log(str(lighting_request.__dict__))

            self.request = lighting_request
            await self.bulb.update()
            await self.operation_callback_by_name[lighting_request.operation]()

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


async def main():
    bulb_controller = BulbController()
    bulb_ip, bulb_topic = os.environ["BULB_IP"], os.environ["BULB_TOPIC"]
    await bulb_controller.create_bulb(bulb_ip, bulb_topic)

    print("Initialization completed successfully.")

    while True:
        try:
            await bulb_controller.async_mqtt()
        except kasa.SmartDeviceException:
            await bulb_controller.bulb_init()


if __name__ == "__main__":
    asyncio.run(main())
