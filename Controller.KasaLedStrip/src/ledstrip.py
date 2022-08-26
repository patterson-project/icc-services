import asyncio
import time
import kasa
import colorsys
from lightingrequest import LightingRequest
from utils import convert_K_to_RGB


class LedStripController:
    async def create_strip(self, ip_address: str) -> None:
        self.ip_address: str = ip_address
        self.strip: kasa.SmartLightStrip = None
        await self.strip_init()
        self.sequence_task: asyncio.Task = None
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
        print("Led Strip controller initialization completed successfully.")

    async def strip_init(self) -> kasa.SmartLightStrip:
        try:
            self.strip = kasa.SmartLightStrip(self.ip_address)
            await (self.strip.update())
        except kasa.SmartDeviceException:
            print("SmartDeviceException: Unable to establish connection with device.")

    def set_request(self, request: LightingRequest) -> None:
        self.request = request

    def terminate_task(self) -> None:
        if self.sequence_task is not None:
            self.sequence_task.cancel()
            self.sequence_task = None

    async def on(self):
        self.terminate_task()
        await self.strip.turn_on()

    async def off(self):
        self.terminate_task()
        await self.strip.turn_off()

    async def hsv(self):
        self.terminate_task()
        await self.strip.set_hsv(
            int(self.request.h), int(self.request.s), int(self.request.v)
        )

    async def brightness(self):
        if self.sequence_task is None:
            await self.strip.set_brightness(self.request.brightness)
        else:
            last_sequence = self.sequence_task.get_name()
            self.terminate_task()
            await self.strip.set_brightness(self.request.brightness)
            await self.operation_callback_by_name[last_sequence]()

    async def temperature(self):
        self.terminate_task()
        (r, g, b) = convert_K_to_RGB(self.request.temperature)
        (r, g, b) = (r / 255, g / 255, b / 255)
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        await self.strip.set_hsv(
            int(h*360), int(s *
                            100), int(v*100)
        )

    async def rainbow(self):
        self.terminate_task()
        self.sequence_task = asyncio.ensure_future(self.rainbow_loop())
        self.sequence_task.set_name("rainbow")

    async def rainbow_loop(self):
        while True:
            for i in range(359):
                await self.strip.set_hsv(i, 100, 100)
                time.sleep(0.05)
