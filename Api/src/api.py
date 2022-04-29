from flask import Flask, Response, request
from flask_cors import CORS
from paho.mqtt.client import Client
from utils import LightingRequest
import json

app = Flask("__main__")
CORS(app)

BROKER_ADDRESS = "10.0.0.35"
BROKER_PORT = 1883


@app.route("/")
def index() -> Response:
    return Response(status=200)


@app.route("/lighting/ledstrip", methods=["POST"])
def led_strip() -> Response:
    body = request.get_json()
    try:
        led_request = LightingRequest(**body)
        publish_lighting_request(led_request, "led-strip")
    except:
        return Response("Invalid JSON body in request.", 400)

    return Response(status=200)


@app.route("/lighting/bulb1", methods=["POST"])
def bulb_1() -> Response:
    body = request.get_json()
    try:
        led_request = LightingRequest(**body)
        publish_lighting_request(led_request, "bulb-1")
    except:
        return Response("Invalid JSON body in request.", 400)

    return Response(status=200)


@app.route("/lighting/bulb2", methods=["POST"])
def bulb_2() -> Response:
    body = request.get_json()
    try:
        led_request = LightingRequest(**body)
        publish_lighting_request(led_request, "bulb-2")
    except:
        return Response("Invalid JSON body in request.", 400)

    return Response(status=200)


def start() -> None:
    app.run(host="0.0.0.0", threaded=True, port=8000)


def get_mqtt_client() -> Client:
    client = Client("api", clean_session=False)
    client.connect(BROKER_ADDRESS, BROKER_PORT)
    return client


def publish_lighting_request(lighting_request: LightingRequest, device: str):
    publish("home/lighting/" + device, json.dumps(lighting_request.__dict__))


def publish(topic, message) -> None:
    client = get_mqtt_client()
    client.publish(topic, message, 1)


if __name__ == "__main__":
    start()
