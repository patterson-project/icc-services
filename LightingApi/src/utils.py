from datetime import datetime, timezone
from json import dumps
from paho.mqtt.client import Client
from os import environ


class LedStripRequest:
    def __init__(
        self,
        operation: str,
        h: int = 0,
        s: int = 100,
        v: int = 50,
        brightness: int = None,
    ):
        self.operation = operation
        self.brightness = brightness
        self.h = h
        self.s = s
        self.v = v


class BulbRequest:
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
        self.client = Client("lighting-api", clean_session=False)
        self.client.connect(environ["BROKER_IP"])

    def publish_lighting_request(
        self, lighting_request: LedStripRequest | BulbRequest, device: str
    ):
        self.publish("home/lighting/" + device,
                     dumps(lighting_request.__dict__))

    def publish(self, topic, message) -> None:
        self.client.publish(topic, message, 1)


def log(message):
    now = datetime.now(timezone.utc).astimezone()
    print("[" + str(now.strftime("%Y-%m-%d %H:%M:%S")) + "]\t", end="")
    print(message)
