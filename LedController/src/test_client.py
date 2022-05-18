import asyncio
import aiocoap
import utils
import json


async def main():
    protocol = await aiocoap.Context.create_client_context()
    lr = utils.LightingRequestResource("Jawn", 1, 2, 3)
    p = bytes(json.dumps(lr.__dict__).encode("utf-8"))
    request = aiocoap.Message(
        code=aiocoap.POST, payload=p, uri="coap://localhost/lightingrequest"
    )

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print("Failed to fetch resource:")
        print(e)
    else:
        print("Result: %s\n%r" % (response.code, response.payload))


if __name__ == "__main__":
    asyncio.run(main())
