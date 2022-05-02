from colorsys import hsv_to_rgb
from json import loads
from multiprocessing import Process
from paho.mqtt.client import Client
from rpi_ws281x import Adafruit_NeoPixel
from time import time
from utils import LightingRequest, LedStripConfig, log, wheel


class LedStripController:
    BROKER_ADDRESS = "10.0.0.35"

    def __init__(self) -> None:
        self.strip: Adafruit_NeoPixel = self.led_strip_init()
        self.client: Client = self.mqtt_init()
        self.sequence_process: Process = None
        self.request: LightingRequest = None
        self.operation_callback_by_name = {
            "off": self.off,
            "hsv": self.hsv,
            "brightness": self.brightness,
            "rainbow": self.rainbow,
            "rainbow_cycle": self.rainbow_cycle,
        }

    def led_strip_init(self) -> Adafruit_NeoPixel:
        strip = Adafruit_NeoPixel(
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

    def mqtt_init(self) -> Client:
        client = Client("led-controller", clean_session=False)
        client.connect(self.BROKER_ADDRESS)
        client.on_message = self.on_message
        client.subscribe("home/lighting/led-strip")
        return client

    def terminate_process(self) -> None:
        if self.sequence_process is not None:
            self.sequence_process.terminate()
            self.sequence_process.join()
            self.sequence_process = None

    def on_message(self, client, userdata, message) -> None:
        lighting_request = LightingRequest(**loads(message.payload))
        log(message.topic, str(lighting_request.__dict__))

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

    def off(self):
        self.terminate_process()
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColorRGB(i, 0, 0, 0)
        self.strip.show()

    def hsv(self):
        self.terminate_process()

        r, g, b = tuple(
            round(i * 255)
            for i in hsv_to_rgb(
                self.request.h / 360, self.request.s / 100, self.request.v / 100
            )
        )

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColorRGB(i, r, b, g)

        self.strip.show()

    def rainbow(self) -> None:
        self.terminate_process()
        self.sequence_process = Process(target=self.rainbow_loop)
        self.sequence_process.name = "rainbow"
        self.sequence_process.start()

    def rainbow_loop(self) -> None:
        while True:
            for j in range(255):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, wheel((i + j) & 255))
                self.strip.show()
                time.sleep(self.request.delay / 1000.0)

    def rainbow_cycle(self):
        self.terminate_process()
        self.sequence_process = Process(target=self.rainbow_cycle_loop)
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
                time.sleep(self.delay / 1000.0)


if __name__ == "__main__":
    led_controller = LedStripController()
    print("Initialization completed successfully.")

    try:
        led_controller.client.loop_forever()
    except SystemError as e:
        led_controller.client.loop_stop()
