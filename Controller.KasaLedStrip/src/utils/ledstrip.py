import asyncio
import time
import kasa
import colorsys
from icc.models import LightingRequestDto
from fastapi import HTTPException
from utils.color import convert_K_to_RGB


class LedStrip:
    async def create_strip(self, ip_address: str) -> None:
        self.ip_address: str = ip_address
        self.strip: kasa.SmartLightStrip = None
        self.sequence_task: asyncio.Task = None
        self.sequence_cancel_event: asyncio.Event = asyncio.Event()
        await self.led_strip_init()

    async def led_strip_init(self) -> kasa.SmartLightStrip:
        try:
            self.strip = kasa.SmartLightStrip(self.ip_address)
            await (self.strip.update())
            print(f"{self.ip_address} initialized")
        except kasa.SmartDeviceException:
            print(
                f"Unable to establish connection to Kasa Led Strip at {self.ip_address}."
            )

    async def execute_request(self, lighting_request: LightingRequestDto) -> None:
        try:
            operation = getattr(self, lighting_request.operation)
            await operation(lighting_request)
        except AttributeError:
            raise HTTPException(
                status_code=400, detail="Invalid Kasa Plug operation invoked"
            )

    async def terminate_task(self) -> None:
        if self.sequence_task is not None:
            self.sequence_cancel_event.clear()
            await self.sequence_task
            self.sequence_task = None

    async def on(self, lighting_request: LightingRequestDto):
        if self.sequence_task is None:
            await self.strip.turn_on()
        else:
            operation = getattr(self, self.sequence_task.get_name())
            await operation(lighting_request)

    async def off(self, lighting_request: LightingRequestDto):
        del lighting_request

        if self.sequence_task is not None:
            self.sequence_cancel_event.clear()
            await self.sequence_task

        await self.strip.turn_off()

    async def hsv(self, lighting_request: LightingRequestDto):
        await self.terminate_task()
        await self.strip.set_hsv(
            int(lighting_request.h), int(lighting_request.s), int(lighting_request.v)
        )

        if lighting_request.brightness is not None:
            await self.strip.set_brightness(lighting_request.brightness)

    async def brightness(self, lighting_request: LightingRequestDto):
        await self.strip.set_brightness(lighting_request.brightness)

    async def temperature(self, lighting_request: LightingRequestDto):
        await self.terminate_task()
        (r, g, b) = convert_K_to_RGB(lighting_request.temperature)
        (r, g, b) = (r / 255, g / 255, b / 255)
        (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
        await self.strip.set_hsv(int(h * 360), int(s * 100), int(v * 100))

        if lighting_request.brightness is not None:
            await self.strip.set_brightness(lighting_request.brightness)

    async def rainbow(self, lighting_request: LightingRequestDto):
        del lighting_request
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
