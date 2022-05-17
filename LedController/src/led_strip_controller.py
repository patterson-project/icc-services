import colorsys
import json
import multiprocessing
import paho.mqtt.client as PahoMqtt
import rpi_ws281x
import time
import os
from utils import LedStripRequest, LedStripConfig, log, wheel, convert_K_to_RGB


class LedStripController:
    def __init__(self) -> None:
        self.strip: rpi_ws281x.Adafruit_NeoPixel = self.led_strip_init()
        self.client: PahoMqtt.Client = self.mqtt_init()
        self.sequence_process: multiprocessing.Process = None
        self.request: LedStripRequest = None
        self.operation_callback_by_name = {
            "on": self.on,
            "off": self.off,
            "hsv": self.hsv,
            "brightness": self.brightness,
            "temperature": self.temperature,
            "rainbow": self.rainbow,
            "rainbow_cycle": self.rainbow_cycle,
        }

    def led_strip_init(self) -> rpi_ws281x.Adafruit_NeoPixel:
        strip = rpi_ws281x.Adafruit_NeoPixel(
            LedStripConfig.COUNT,
            LedStripConfig.PIN,
            LedStripConfig.FREQ_HZ,
            LedStripConfig.DMA,
            LedStripConfig.INVERT,
            LedStripConfig.BRIGHTNESS,
            LedStripConfig.CHANNEL,
        )
        strip.begin()
        return strip

    def mqtt_init(self) -> PahoMqtt.Client:
        client = PahoMqtt.Client("led-controller", clean_session=False)
        client.connect(
            host=os.environ["BROKER_IP"], port=int(os.environ["BROKER_PORT"])
        )
        client.on_message = self.on_message
        client.subscribe("home/lighting/led-strip")
        return client

    def terminate_process(self) -> None:
        if self.sequence_process is not None:
            self.sequence_process.terminate()
            self.sequence_process.join()
            self.sequence_process = None

    def on_message(self, client, userdata, message) -> None:
        lighting_request = LedStripRequest(**json.loads(message.payload))
        log(str(lighting_request.__dict__))

        self.request = lighting_request
        self.operation_callback_by_name[lighting_request.operation]()

    def brightness(self):
        if self.sequence_process is None:
            self.strip.setBrightness(int(255 * (int(self.request.brightness) / 100)))
            self.strip.show()
        else:
            last_sequence = self.sequence_process.name
            self.terminate_process()
            self.strip.setBrightness(int(255 * (int(self.request.brightness) / 100)))
            self.strip.show()
            self.operation_callback_by_name[last_sequence]()

    def temperature(self):
        self.terminate_process()

        r, g, b = convert_K_to_RGB(self.request.temperature)

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColorRGB(i, r, b, g)

        self.strip.show()

    def on(self):
        self.terminate_process()
        self.strip.setBrightness(255)
        self.strip.show()

    def off(self):
        self.terminate_process()
        self.strip.setBrightness(0)
        self.strip.show()

    def hsv(self):
        self.terminate_process()

        r, g, b = tuple(
            round(i * 255)
            for i in colorsys.hsv_to_rgb(
                self.request.h / 360, self.request.s / 100, self.request.v / 100
            )
        )

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColorRGB(i, r, b, g)

        self.strip.show()

    def rainbow(self) -> None:
        self.terminate_process()
        self.sequence_process = multiprocessing.Process(target=self.rainbow_loop)
        self.sequence_process.name = "rainbow"
        self.sequence_process.start()

    def rainbow_loop(self) -> None:
        while True:
            for j in range(255):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, wheel((i + j) & 255))
                self.strip.show()
                time.sleep(0.05)

    def rainbow_cycle(self):
        self.terminate_process()
        self.sequence_process = multiprocessing.Process(target=self.rainbow_cycle_loop)
        self.sequence_process.name = "rainbow_cycle"
        self.sequence_process.start()

    def rainbow_cycle_loop(self) -> None:
        while True:
            for j in range(255):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(
                        i, wheel((int(i * 256 / self.strip.numPixels()) + j) & 255)
                    )
                self.strip.show()
                time.sleep(0.05)


if __name__ == "__main__":
    led_controller = LedStripController()
    print("Initialization completed successfully.")

    try:
        led_controller.client.loop_forever()
    except SystemError as e:
        led_controller.client.loop_stop()
