import kasa
from icc.models import PowerRequestDto
from fastapi import HTTPException


class Plug:
    async def create_plug(self, ip_address: str) -> None:
        self.ip_address: str = ip_address
        self.plug: kasa.SmartPlug = None
        await self.plug_init()

    async def plug_init(self) -> kasa.SmartPlug:
        try:
            self.plug = kasa.SmartPlug(self.ip_address)
            await self.plug.update()
            print(f"{self.ip_address} initialized")
        except kasa.SmartDeviceException:
            print(
                f"Unable to establish connection to Kasa Plug at {self.ip_address}")

    async def execute_request(self, power_request: PowerRequestDto) -> None:
        try:
            operation = getattr(self, power_request.operation)
            await operation(power_request)
        except AttributeError:
            raise HTTPException(
                status_code=400, detail="Invalid Kasa Led Strip operation invoked")

    async def on(self, power_request: PowerRequestDto) -> None:
        del power_request
        await self.plug.turn_on()

    async def off(self, power_request: PowerRequestDto) -> None:
        del power_request
        await self.plug.turn_off()
