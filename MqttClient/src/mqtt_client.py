import json
import paho.mqtt.client as mqtt
import led_operation
from rpi_ws281x import *
from multiprocessing import Process
from utils import LedRequest, TerminalColors, LedConfig, log


class MqttClient:

    def __init__(self):
        self.strip = self.led_strip_init()
        self.client = self.mqtt_init()
        self.led_process = None

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
        client = mqtt.Client("LedPi")
        client.connect(LedConfig.BROKER_ADDRESS)
        client.on_message = self.on_message
        client.subscribe("leds")
        return client

    def on_message(self, client, userdata, message) -> None:
        led_request = LedRequest(**json.loads(message.payload))

        log(message.topic, str(led_request.__dict__))

        if self.led_process is not None:
            self.led_process.terminate()

        try:
            if led_request.operation == "rgb":
                self.led_process = Process(target=getattr(
                    led_operation, led_request.operation), args=(self.strip, led_request.r, led_request.g, led_request.b,))
            else:
                self.led_process = Process(target=getattr(
                    led_operation, led_request.operation), args=(self.strip,))
            self.led_process.start()

        except AttributeError as e:
            print(
                f"{TerminalColors.WARNING}ERROR:\n {e.message}{TerminalColors.ENDC}")


if __name__ == '__main__':
    mqtt_client = MqttClient()
    print("Initialization complete.")

    try:
        mqtt_client.client.loop_forever()
    except SystemError as e:
        mqtt_client.client.loop_stop()
