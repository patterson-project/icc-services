import kasa
from icc.models import PowerRequest


class Plug:
    async def create_plug(self, ip_address: str) -> None:
        self.ip_address: str = ip_address
        self.plug: kasa.SmartPlug = None
        await self.strip_init()
        self.request: PowerRequest = None
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

    def set_request(self, request: PowerRequest) -> None:
        self.request = request

    async def on(self):
        await self.plug.turn_on()

    async def off(self):
        await self.plug.turn_off()
