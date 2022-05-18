import asyncio
import aiocoap
import utils
import json


async def main():
    protocol = await aiocoap.Context.create_client_context()
    lr = utils.LightingRequest("Jawn", 1, 2, 3)
    p = bytes(json.dumps(lr.__dict__).encode("utf-8"))
    request = aiocoap.Message(code=aiocoap.GET, uri="coap://10.0.0.68/health")

    response = await protocol.request(request).response
    print("Result: %s\n%r" % (response.code, response.payload))


if __name__ == "__main__":
    asyncio.run(main())
