from flask import Flask, Response, request
from flask_cors import CORS
from paho.mqtt.client import Client
from utils import LedRequest
import json

app = Flask("__main__")
CORS(app)

BROKER_ADDRESS = "10.0.0.35"
BROKER_PORT = 1883


@app.route("/")
def index() -> Response:
    return Response(status=200)


@app.route("/lighting", methods=["POST"])
def lighting() -> Response:
    body = request.get_json()
    try:
        led_request = LedRequest(**body)
        publish("home/lighting", json.dumps(led_request.__dict__))
    except:
        return Response("Invalid JSON body in request.", 400)

    return Response(status=200)


def start():
    app.run(host="0.0.0.0", threaded=True, port=8000)


def get_mqtt_client() -> Client:
    client = Client("api", clean_session=False)
    client.connect(BROKER_ADDRESS, BROKER_PORT)
    return client


def publish(topic, message) -> None:
    client = get_mqtt_client()
    client.publish(topic, message, 1)


if __name__ == "__main__":
    start()
