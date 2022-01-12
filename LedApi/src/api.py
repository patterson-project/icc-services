from flask import Flask, Response, request
from flask_cors import CORS
from paho.mqtt.client import Client
from utils import LedRequest, log
import json

app = Flask("__main__")
CORS(app)

BROKER_ADDRESS = "10.0.0.35"
BROKER_PORT = 1883


@app.route("/")
def index() -> Response:
    return Response(status=200)


@app.route("/off")
def off() -> Response:
    led_request = LedRequest("off")
    publish("leds", json.dumps(led_request.__dict__))
    return Response(status=200)


@app.route("/brightness", methods=["POST"])
def brightness() -> Response:
    body = request.get_json()
    led_request = LedRequest(**body)
    publish("leds", json.dumps(led_request.__dict__))
    return Response(status=200)


@app.route("/rgb", methods=["POST"])
def rgb() -> Response:
    body = request.get_json()
    led_request = LedRequest(**body)
    publish("leds", json.dumps(led_request.__dict__))
    return Response(status=200)


@app.route("/colorwipe")
def color_wipe() -> Response:
    led_request = LedRequest("color_wipe")
    publish("leds", json.dumps(led_request.__dict__))
    return Response(status=200)


@app.route("/theaterchase")
def theater_chase() -> Response:
    led_request = LedRequest("theater_chase")
    publish("leds", json.dumps(led_request.__dict__))
    return Response(status=200)


@app.route("/rainbow")
def rainbow() -> Response:
    led_request = LedRequest("rainbow")
    publish("leds", json.dumps(led_request.__dict__))
    return Response(status=200)


@app.route("/rainbowcycle")
def rainbow_cycle() -> Response:
    led_request = LedRequest("rainbow_cycle")
    publish("leds", json.dumps(led_request.__dict__))
    return Response(status=200)


@app.route("/theaterchaserainbow")
def theater_chase_rainbow() -> Response:
    led_request = LedRequest("theater_chase_rainbow")
    publish("leds", json.dumps(led_request.__dict__))
    return Response(status=200)


@app.route("/sunrise")
def sunrise() -> Response:
    led_request = LedRequest("sunrise")
    publish("leds", json.dumps(led_request.__dict__))
    return Response(status=200)


def start():
    app.run(host='0.0.0.0', threaded=True, port=8000, debug=True)


def get_mqtt_client() -> Client:
    client = Client("ApiPi")
    client.connect(BROKER_ADDRESS, BROKER_PORT)
    return client


def publish(topic, message) -> None:
    client = get_mqtt_client()
    client.publish(topic, message)


start()
