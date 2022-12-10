import kasa
from icc.models import PowerRequestDto


class Plug:
    async def create_plug(self, ip_address: str) -> None:
        self.ip_address: str = ip_address
        self.plug: kasa.SmartPlug = None
        await self.strip_init()
        self.operation_callback_by_name = {
            "on": self.on,
            "off": self.off,
        }
        print(f"{self.ip_address} initialized")

    async def strip_init(self) -> kasa.SmartPlug:
        try:
            self.plug = kasa.SmartPlug(self.ip_address)
            await self.plug.update()
        except kasa.SmartDeviceException:
            print("SmartDeviceException: Unable to establish connection with device.")

    async def execute_request(self, power_request: PowerRequestDto) -> None:
        await locals()[power_request.operation]()

    async def on(self) -> None:
        await self.plug.turn_on()

    async def off(self) -> None:
        await self.plug.turn_off()
