from flask import Flask, Response
from paho.mqtt.client import Client

app = Flask("__main__")
BROKER_ADDRESS = "10.0.0.35"


@app.route("/")
def index() -> Response:
    return Response(status=200)


@app.route("/off")
def off() -> Response:
    publish("leds", "off")
    return Response(status=200)


@app.route("/colorwipe")
def color_wipe() -> Response:
    publish("leds", "color_wipe")
    return Response(status=200)


@app.route("/theaterchase")
def theater_chase() -> Response:
    publish("leds", "theater_chase")
    return Response(status=200)


@app.route("/rainbow")
def rainbow() -> Response:
    publish("leds", "rainbow")
    return Response(status=200)


@app.route("/rainbowcycle")
def rainbow_cycle() -> Response:
    publish("leds", "rainbow_cycle")
    return Response(status=200)


@app.route("/theaterchaserainbow")
def theater_chase_rainbow() -> Response:
    publish("leds", "theater_chase_rainbow")
    return Response(status=200)


def start():
    app.run(host='0.0.0.0', threaded=True, port=8000, debug=True)


def get_mqtt_client() -> Client:
    client = Client("ApiPi")
    client.connect(BROKER_ADDRESS)
    return client


def publish(topic, message) -> None:
    client = get_mqtt_client()
    client.publish(topic, message)


start()
