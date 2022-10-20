import asyncio
import math
import time
import kasa
import colorsys
from lightingrequest import LightingRequest


class LedStrip:
    async def create_strip(self, ip_address: str) -> None:
        self.ip_address: str = ip_address
        self.strip: kasa.SmartLightStrip = None
        await self.strip_init()
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

    async def strip_init(self) -> kasa.SmartLightStrip:
        try:
            self.strip = kasa.SmartLightStrip(self.ip_address)
            await (self.strip.update())
        except kasa.SmartDeviceException:
            print("SmartDeviceException: Unable to establish connection with device.")

    def set_request(self, request: LightingRequest) -> None:
        self.request = request

    async def terminate_task(self) -> None:
        if self.sequence_task is not None:
            self.sequence_cancel_event.clear()
            await self.sequence_task
            self.sequence_task = None

    async def on(self):
        if self.sequence_task is None:
            await self.strip.turn_on()
        else:
            await self.operation_callback_by_name[self.sequence_task.get_name()]()

    async def off(self):
        if self.sequence_task is not None:
            self.sequence_cancel_event.clear()
            await self.sequence_task

        await self.strip.turn_off()

    async def hsv(self):
        await self.terminate_task()
        await self.strip.set_hsv(
            int(self.request.h), int(self.request.s), int(self.request.v)
        )

    async def brightness(self):
        await self.strip.set_brightness(self.request.brightness)

    async def temperature(self):
        await self.terminate_task()
        (r, g, b) = self.convert_K_to_RGB(self.request.temperature)
        (r, g, b) = (r / 255, g / 255, b / 255)
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        await self.strip.set_hsv(
            int(h*360), int(s *
                            100), int(v*100)
        )

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

                await self.strip.set_hsv(i, 100, 100)
                time.sleep(0.05)

    def convert_K_to_RGB(self, colour_temperature) -> tuple[int, int, int]:
        # range check
        if colour_temperature < 1000:
            colour_temperature = 1000
        elif colour_temperature > 40000:
            colour_temperature = 40000

        tmp_internal = colour_temperature / 100.0

        # red
        if tmp_internal <= 66:
            red = 255
        else:
            tmp_red = 329.698727446 * \
                math.pow(tmp_internal - 60, -0.1332047592)
            if tmp_red < 0:
                red = 0
            elif tmp_red > 255:
                red = 255
            else:
                red = tmp_red

        # green
        if tmp_internal <= 66:
            tmp_green = 99.4708025861 * math.log(tmp_internal) - 161.1195681661
            if tmp_green < 0:
                green = 0
            elif tmp_green > 255:
                green = 255
            else:
                green = tmp_green
        else:
            tmp_green = 288.1221695283 * \
                math.pow(tmp_internal - 60, -0.0755148492)
            if tmp_green < 0:
                green = 0
            elif tmp_green > 255:
                green = 255
            else:
                green = tmp_green

        # blue
        if tmp_internal >= 66:
            blue = 255
        elif tmp_internal <= 19:
            blue = 0
        else:
            tmp_blue = 138.5177312231 * \
                math.log(tmp_internal - 10) - 305.0447927307
            if tmp_blue < 0:
                blue = 0
            elif tmp_blue > 255:
                blue = 255
            else:
                blue = tmp_blue

        return int(red), int(green), int(blue)
