import paho.mqtt.client as mqtt
import led_operation
from rpi_ws281x import *
from multiprocessing import Process
from utils import TerminalColors, LedConfig


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
        client.loop_forever()
        client.subscribe("leds")
        return client

    def on_message(self, client, userdata, message) -> None:
        operation = message.payload.decode("utf-8")

        print("MESSAGE:\t", str(message.payload.decode("utf-8")))
        print("TOPIC:\t", message.topic)

        if self.led_process is not None:
            self.led_process.terminate()

        try:
            self.led_process = Process(target=getattr(
                led_operation, operation), args=(self.strip,))
            self.led_process.start()

        except AttributeError as e:
            print(
                f"{TerminalColors.WARNING}ERROR:\n {e.message}{TerminalColors.ENDC}")


if __name__ == '__main__':
    mqtt_client = MqttClient()
    print("Initialization complete.")

    try:
        while True:
            continue
    except SystemError as e:
        mqtt_client.client.loop_stop()
