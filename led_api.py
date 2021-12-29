from flask import Flask
from rpi_ws281x import *
from led_operations import *
from led_config import LedConfig as conf
import json
import requests

app = Flask("__main__")


@app.route("/")
def index():
    strip = Adafruit_NeoPixel(
        conf.LED_COUNT, conf.LED_PIN, conf.LED_FREQ_HZ, conf.LED_DMA, conf.LED_INVERT, conf.LED_BRIGHTNESS, conf.LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    while True:
        print('Color wipe animations.')
        colorWipe(strip, Color(255, 0, 0))  # Red wipe
        colorWipe(strip, Color(0, 255, 0))  # Blue wipe
        colorWipe(strip, Color(0, 0, 255))  # Green wipe
        print('Theater chase animations.')
        theaterChase(strip, Color(127, 127, 127))  # White theater chase
        theaterChase(strip, Color(127,   0,   0))  # Red theater chase
        theaterChase(strip, Color(0,   0, 127))  # Blue theater chase
        print('Rainbow animations.')
        rainbow(strip)
        rainbowCycle(strip)
        theaterChaseRainbow(strip)


def start():
    app.run(host='0.0.0.0', threaded=True, port=5000, debug=True)


start()
