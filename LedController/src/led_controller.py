import json
from multiprocessing.process import current_process
import time
from kasa import SmartBulb
import paho.mqtt.client as mqtt
import colorsys
from rpi_ws281x import Adafruit_NeoPixel
from multiprocessing import Process
from utils import LedRequest, LedConfig, log
from rpi_ws281x import Color
from sequences import LedStripSequence


class LedController:
    def __init__(self):
        self.strip = self.led_strip_init()
        self.client = self.mqtt_init()
        self.led_process = None
        self.sequence = LedStripSequence()
        self.request = None
        self.operation_callback = {
            "hsla": self.hsla,
            "brightness": self.brightness,
            "rainbow": self.rainbow,
            "color_wipe": self.color_wipe,
            "sunrise": self.sunrise,
            "theater_chase": self.theater_chase,
            "rainbow_cycle": self.rainbow_cycle,
            "theater_chase_rainbow": self.theater_chase_rainbow,
        }

    def led_strip_init(self) -> Adafruit_NeoPixel:
        strip = Adafruit_NeoPixel(
            LedConfig.COUNT,
            LedConfig.PIN,
            LedConfig.FREQ_HZ,
            LedConfig.DMA,
            LedConfig.INVERT,
            LedConfig.BRIGHTNESS,
            LedConfig.CHANNEL,
        )
        strip.begin()
        return strip

    def mqtt_init(self) -> mqtt.Client:
        client = mqtt.Client("led-controller", clean_session=False)
        client.connect(LedConfig.BROKER_ADDRESS)
        client.on_message = self.on_message
        client.subscribe("home/lighting")
        return client

    def terminate_process(self) -> None:
        if self.led_process is not None:
            self.led_process.terminate()
            self.led_process.join()
            self.led_process = None

    def on_message(self, client, userdata, message) -> None:
        led_request = LedRequest(**json.loads(message.payload))
        log(message.topic, str(led_request.__dict__))

        self.terminate_process()
        self.request = led_request
        self.operation_callback[led_request.operation]()

    def brightness(self):
        pass

    def hsla(self):
        r, g, b = tuple(
            round(i * 255)
            for i in colorsys.hls_to_rgb(
                self.request.h / 360, self.request.l / 100, self.request.s / 100
            )
        )

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColorRGB(i, r, b, g)
            self.strip.show()
            time.sleep(50 / 1000.0)

    def rainbow(self, wait_ms=20) -> None:
        self.terminate_process()
        self.led_process = Process(
            target=self.sequence.rainbow, args=(self.strip, self.request.wait_ms)
        )
        self.led_process.name = self.request.operation
        self.led_process.start()

    def color_wipe(self):
        pass

    def sunrise(self):
        pass

    def theater_chase(self):
        pass

    def rainbow_cycle(self):
        pass

    def theater_chase_rainbow(self):
        pass


if __name__ == "__main__":
    mqtt_client = LedController()
    print("Initialization completed successfully.")

    try:
        mqtt_client.client.loop_forever()
    except SystemError as e:
        mqtt_client.client.loop_stop()
