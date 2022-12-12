import asyncio
import time
import kasa
from icc.models import LightingRequest


class Bulb:
    async def create_bulb(self, ip_address: str) -> None:
        self.ip_address: str = ip_address
        self.bulb: kasa.SmartBulb = None
        await self.bulb_init()
        self.sequence_task: asyncio.Task = None
        self.sequence_cancel_event: asyncio.Event = asyncio.Event()
        self.request: LightingRequest = None
        self.operation_callback_by_name = {
            "on": self.on,
            "off": self.off,
            "hsv": self.hsv,
            "brightness": self.brightness,
            "rainbow": self.rainbow,
            "rainbow_cycle": self.rainbow,
            "temperature": self.temperature,
        }
        print(f"{self.ip_address} initialized")

    async def bulb_init(self) -> kasa.SmartBulb:
        try:
            self.bulb = kasa.SmartBulb(self.ip_address)
            await (self.bulb.update())
        except kasa.SmartDeviceException:
            print("Unable to establish connection with device.")

    def set_request(self, request: LightingRequest) -> None:
        self.request = request

    async def terminate_task(self) -> None:
        if self.sequence_task is not None:
            self.sequence_cancel_event.clear()
            await self.sequence_task
            self.sequence_task = None

    async def on(self):
        if self.sequence_task is None:
            await self.bulb.turn_on()
        else:
            await self.operation_callback_by_name[self.sequence_task.get_name()]()

    async def off(self):
        if self.sequence_task is not None:
            self.sequence_cancel_event.clear()
            await self.sequence_task

        await self.bulb.turn_off()

    async def hsv(self):
        await self.terminate_task()
        await self.bulb.set_hsv(
            int(self.request.h), int(self.request.s), int(self.request.v)
        )

    async def brightness(self):
        await self.bulb.set_brightness(self.request.brightness)

    async def temperature(self):
        await self.terminate_task()
        await self.bulb.set_color_temp(int(self.request.temperature))

    async def rainbow(self):
        await self.terminate_task()
        self.sequence_cancel_event.set()
        self.sequence_task = asyncio.create_task(self.rainbow_loop())
        self.sequence_task.set_name("rainbow")

    async def rainbow_loop(self):
        running = True

        while running:
            for i in range(359):
                if not self.sequence_cancel_event.is_set():
                    running = False
                    break

                await self.bulb.set_hsv(i, 100, 100)
                time.sleep(0.05)
