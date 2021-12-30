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


def start():
    client.connect(BROKER_ADDRESS)
    app.run(host='', threaded=True, port=8000, debug=True)


start()
