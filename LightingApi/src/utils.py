import datetime
import json
import aiocoap
import paho.mqtt.client as MqttClient
import os


class LightingRequest:
    def __init__(
        self,
        operation: str,
        h: int = 0,
        s: int = 100,
        v: int = 50,
        brightness: int = None,
        temperature: int = None,
    ):
        self.operation = operation
        self.brightness = brightness
        self.h = h
        self.s = s
        self.v = v
        self.temperature = temperature


class LightingMqttClient:
    def __init__(self) -> None:
        self.client = MqttClient.Client("lighting-api", clean_session=False)
        self.client.connect(
            host=os.environ["BROKER_IP"], port=int(os.environ["BROKER_PORT"])
        )

    def publish_lighting_request(self, lighting_request: LightingRequest, device: str):
        self.publish("home/lighting/" + device, json.dumps(lighting_request.__dict__))

    def publish(self, topic, message) -> None:
        self.client.publish(topic, message, 1)


class CoapUri:
    LED_STRIP_URI = "coap://10.0.0.68/lightingrequest"


class CoapRequest:
    def __init__(self):
        self.protocol: aiocoap.Context = None

    async def init_coap_protocol(self):
        self.protocol = await aiocoap.Context.create_client_context()

    async def post(self, payload: any, dest_uri: str) -> tuple[str, str]:
        payload_bytes = bytes(json.dumps(payload.__dict__).encode("utf-8"))
        request = aiocoap.Message(
            code=aiocoap.POST, payload=payload_bytes, uri=dest_uri
        )

        try:
            response = await self.protocol.request(request).response
        except Exception as e:
            print("Failed to fetch resource:")
            print(e)
        else:
            return (response.code, response.payload)


def log(message):
    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    print("[" + str(now.strftime("%Y-%m-%d %H:%M:%S")) + "]\t", end="")
    print(message)
