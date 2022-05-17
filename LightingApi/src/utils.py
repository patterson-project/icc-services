import datetime
import json
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
            host=os.environ["BROKER_IP"], port=os.environ["BROKER_PORT"]
        )

    def publish_lighting_request(self, lighting_request: LightingRequest, device: str):
        self.publish("home/lighting/" + device, json.dumps(lighting_request.__dict__))

    def publish(self, topic, message) -> None:
        self.client.publish(topic, message, 1)


def log(message):
    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    print("[" + str(now.strftime("%Y-%m-%d %H:%M:%S")) + "]\t", end="")
    print(message)
