import colorsys
import multiprocessing
import rpi_ws281x
import time
from utils import wheel, convert_K_to_RGB
from ledstripconfig import LedStripConfig
from lightingrequest import LightingRequest


class LedStripController:
    def __init__(self) -> None:
        self.strip: rpi_ws281x.Adafruit_NeoPixel = self.led_strip_init()
        self.sequence_process: multiprocessing.Process = None
        self.request: LightingRequest = None
        self.last_rgb: tuple[int, int, int] = (255, 255, 255)
        self.operation_callback_by_name = {
            "on": self.on,
            "off": self.off,
            "hsv": self.hsv,
            "brightness": self.brightness,
            "temperature": self.temperature,
            "rainbow": self.rainbow,
            "rainbow_cycle": self.rainbow_cycle,
        }
        print("Controller initialization completed successfully.")

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

    def set_request(self, request: LightingRequest):
        self.request = request

    def terminate_process(self) -> None:
        if self.sequence_process is not None:
            self.sequence_process.terminate()
            self.sequence_process.join()
            self.sequence_process = None

    def brightness(self):
        if self.sequence_process is None:
            self.strip.setBrightness(
                int(255 * (int(self.request.brightness) / 100)))
            self.strip.show()
        else:
            last_sequence = self.sequence_process.name
            self.terminate_process()
            self.strip.setBrightness(
                int(255 * (int(self.request.brightness) / 100)))
            self.strip.show()
            self.operation_callback_by_name[last_sequence]()

    def temperature(self):
        self.terminate_process()

        r, g, b = convert_K_to_RGB(self.request.temperature)
        self.last_rgb = (r, g, b)

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColorRGB(i, r, b, g)

        self.strip.show()

    def on(self):
        self.terminate_process()

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColorRGB(
                i, self.last_rgb[0], self.last_rgb[2], self.last_rgb[1]
            )
        self.strip.show()

    def off(self):
        self.terminate_process()

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColorRGB(i, 0, 0, 0)
        self.strip.show()

    def hsv(self):
        self.terminate_process()

        r, g, b = tuple(
            round(i * 255)
            for i in colorsys.hsv_to_rgb(
                self.request.h / 360, self.request.s / 100, self.request.v / 100
            )
        )
        self.last_rgb = (r, g, b)

        for i in range(self.strip.numPixels()):
            self.strip.setPixelColorRGB(i, r, b, g)

        self.strip.show()

    def rainbow(self) -> None:
        self.terminate_process()
        self.sequence_process = multiprocessing.Process(
            target=self.rainbow_loop)
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
        self.sequence_process = multiprocessing.Process(
            target=self.rainbow_cycle_loop)
        self.sequence_process.name = "rainbow_cycle"
        self.sequence_process.start()

    def rainbow_cycle_loop(self) -> None:
        while True:
            for j in range(255):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(
                        i, wheel(
                            (int(i * 256 / self.strip.numPixels()) + j) & 255)
                    )
                self.strip.show()
                time.sleep(0.05)
