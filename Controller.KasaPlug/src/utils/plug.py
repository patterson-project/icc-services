import kasa
from icc.models import PowerRequestDto, DeviceModel, PydanticObjectId
from server.database import DeviceRepository


class Plug:
    async def create_plug(self, ip_address: str) -> None:
        self.ip_address: str = ip_address
        self.plug: kasa.SmartPlug = None
        self.operation_callback_by_name = {
            "on": self.on,
            "off": self.off,
        }
        await self.strip_init()

    async def strip_init(self) -> kasa.SmartPlug:
        try:
            self.plug = kasa.SmartPlug(self.ip_address)
            await self.plug.update()
            print(f"{self.ip_address} initialized")
        except kasa.SmartDeviceException:
            print("SmartDeviceException: Unable to establish connection with device.")

    async def execute_request(self, power_request: PowerRequestDto) -> None:
        await locals()[power_request.operation]()

    async def on(self) -> None:
        await self.plug.turn_on()

    async def off(self) -> None:
        await self.plug.turn_off()


async def initialize_plugs(device_repository: DeviceRepository):
    kasa_plugs: list[DeviceModel] = device_repository.find_all_kasa_plugs()
    plugs: dict[PydanticObjectId, Plug] = {}

    for device in kasa_plugs:
        plug = Plug()
        await plug.create_plug(device.ip)
        plugs[device.id] = plug

    return plugs
