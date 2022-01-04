from flask import Flask, Response
import paho.mqtt.client as mqtt

app = Flask("__main__")
client = mqtt.Client("ApiPi")
BROKER_ADDRESS = "10.0.0.35"


@app.route("/")
def index():
    return Response(status=200)

@app.route("/off")
def off():
    client.publish("leds", "off")
    return Response(status=200)

@app.route("/colorwipe")
def color_wipe():
    client.publish("leds", "color_wipe")
    return Response(status=200)

@app.route("/theaterchase")
def theater_chase():
    client.publish("leds", "theater_chase")
    return Response(status=200)

@app.route("/rainbow")
def rainbow():
    client.publish("leds", "rainbow")
    return Response(status=200)

@app.route("/rainbowcycle")
def rainbow_cycle():
    client.publish("leds", "rainbow_cycle")
    return Response(status=200)

@app.route("/theaterchaserainbow")
def theater_chase_rainbow():
    client.publish("leds", "theater_chase_rainbow")
    return Response(status=200)

def start():
    client.connect(BROKER_ADDRESS)
    app.run(host='0.0.0.0', threaded=True, port=8000, debug=True)

start()
