import asyncio
import aiocoap
import json
from ledstrip import LedStripController
from utils import log, LightingRequest
from aiocoap import resource

led_controller = LedStripController()


class LightingRequestResource(resource.Resource):
    def __init__(self):
        super().__init__()

    async def render_post(self, request):
        lighting_request = LightingRequest(
            **json.loads(request.payload.decode("utf-8"))
        )
        log(str(lighting_request.__dict__))

        led_controller.request = lighting_request
        led_controller.operation_callback_by_name[lighting_request.operation]()
        return aiocoap.Message(payload=b"Success")


async def main():
    root = resource.Site()
    root.add_resource(["lightingrequest"], LightingRequestResource())

    await aiocoap.Context.create_server_context(root)
    await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
