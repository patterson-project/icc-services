from rpi_ws281x import *
from led_operations import *
from led_config import LedConfig as conf
import paho.mqtt.client as mqtt

broker_address = "10.0.0.35"


def led_strip_init() -> Adafruit_NeoPixel:
    strip = Adafruit_NeoPixel(
        conf.LED_COUNT, conf.LED_PIN, conf.LED_FREQ_HZ, conf.LED_DMA, conf.LED_INVERT, conf.LED_BRIGHTNESS, conf.LED_CHANNEL)
    strip.begin()
    return strip


def mqtt_init() -> mqtt.Client:
    client = mqtt.Client("LedController")
    client.connect(broker_address)
    client.on_message = on_message
    client.loop_start()
    client.subscribe("leds")
    return client


def on_message(client, userdata, message) -> None:
    command = message.payload.decode("utf-8")   

    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

    if command == "ColorWipe":
        print('Color wipe animations.')
        colorWipe(strip, Color(255, 0, 0))  # Red wipe
        colorWipe(strip, Color(0, 255, 0))  # Blue wipe
        colorWipe(strip, Color(0, 0, 255))  # Green wipe
    elif command == "TheaterChase":
        print('Theater chase animations.')
        theaterChase(strip, Color(127, 127, 127))  # White theater chase
        theaterChase(strip, Color(127,   0,   0))  # Red theater chase
        theaterChase(strip, Color(0,   0, 127))  # Blue theater chase
    elif command == "Rainbow":
        print('Rainbow animations.')
        rainbow(strip)
        rainbowCycle(strip)
        theaterChaseRainbow(strip)


if __name__ == '__main__':
    strip = led_strip_init()
    client = mqtt_init()
    
    print("Initialization complete.")
    try:
        while True:
            continue
    except SystemError as e:
        client.loop_stop()
