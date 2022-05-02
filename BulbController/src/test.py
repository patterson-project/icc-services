from paho.mqtt.client import Client
import json
from utils import LightingRequest


def get_mqtt_client() -> Client:
    client = Client("api", clean_session=False)
    client.connect("10.0.0.35")
    return client


def publish_lighting_request(
    client: Client, lighting_request: LightingRequest, device: str
):
    client.publish("home/lighting/" + device, json.dumps(lighting_request.__dict__))


if __name__ == "__main__":
    client = get_mqtt_client()
    publish_lighting_request(client, LightingRequest("hsv", 0, 50, 100), "bulb-1")
