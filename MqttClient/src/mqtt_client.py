import paho.mqtt.client as mqtt

from led_config import LedConfig
from rpi_ws281x import *
from led_operation import *
from led_operation import LedOperation


class MqttClient:

    def __init__(self):
        self.BROKER_ADDRESS = "10.0.0.35"
        self.strip = self.led_strip_init()
        self.client = self.mqtt_init()
        self.led_operation = LedOperation(None, self.strip)

    def led_strip_init(self) -> Adafruit_NeoPixel:
        strip = Adafruit_NeoPixel(
            LedConfig.COUNT,
            LedConfig.PIN,
            LedConfig.FREQ_HZ,
            LedConfig.DMA,
            LedConfig.INVERT,
            LedConfig.BRIGHTNESS,
            LedConfig.CHANNEL)
        strip.begin()
        return strip

    def mqtt_init(self) -> mqtt.Client:
        client = mqtt.Client("LedController")
        client.connect(self.BROKER_ADDRESS)
        client.on_message = self.on_message
        client.loop_start()
        client.subscribe("leds")
        return client

    def on_message(self, client, userdata, message) -> None:
        operation = message.payload.decode("utf-8")

        print("MESSAGE:\t", str(message.payload.decode("utf-8")))
        print("TOPIC:\t", message.topic)

        self.led_operation.terminate()
        self.led_operation = LedOperation(operation, self.strip)
        self.led_operation.run()


if __name__ == '__main__':
    mqtt_client = MqttClient()
    print("Initialization complete.")

    try:
        while True:
            continue
    except SystemError as e:
        mqtt_client.client.loop_stop()
