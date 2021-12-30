from flask import Flask
import paho.mqtt.client as mqtt

app = Flask("__main__")
client = mqtt.Client("ApiPi")
BROKER_ADDRESS = "10.0.0.35"


@app.route("/")
def index():
    return "Hello BODDDDYYYYY"


@app.route("/rainbow")
def rainbow():
    client.publish("leds", "rainbow")


@app.route("/off")
def off():
    client.publish("leds", "off")


def start():
    client.connect(BROKER_ADDRESS)
    app.run(host='0.0.0.0', threaded=True, port=8000, debug=True)


start()
