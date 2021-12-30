from rpi_ws281x import Color
import time
from threading import Thread
from utils import bcolors


class LedOperation:
    def __init__(self, operation_name, strip) -> None:
        self.operation_name = operation_name
        self.strip = strip
        self.executing = True
        self.operation_names = {'off': self.off,
                                'colorWipe': self.color_wipe,
                                'theaterChase': self.theater_chase,
                                'rainbow': self.rainbow,
                                'rainbowCycle': self.rainbow_cycle,
                                'theaterChaseRainbow': self.theater_chase_rainbow}

    def run(self) -> None:
        try:
            operation_thread = Thread(
                target=self.operation_names[self.operation_name])
            operation_thread.start()
            operation_thread.join()
        except KeyError as e:
            print(f"{bcolors.WARNING}ERROR:\n {e.message}{bcolors.ENDC}")

    def terminate(self) -> None:
        self.executing = False

    def off(self) -> None:
        self.strip.setPixelColorRGB(0, 0, 0)

    def color_wipe(self, colors=[Color(255, 0, 0), Color(0, 255, 0), Color(0, 0, 255)], wait_ms=50):
        while self.executing:
            for color in colors:
                self.wipe(color, wait_ms)

    def wipe(self, color, wait_ms=50) -> None:
        """Wipe color across display a pixel at a time."""
        while self.executing:
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, color)
                self.strip.show()
                time.sleep(wait_ms/1000.0)

    def theater_chase(self, color=Color(127, 127, 127), wait_ms=50) -> None:
        """Movie theater light style chaser animation."""
        while self.executing:
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, color)
                self.strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)

    def wheel(self, pos) -> None:
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(self, wait_ms=20) -> None:
        """Draw rainbow that fades across all pixels at once."""
        while self.executing:
            for j in range(255):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(i, self.wheel((i+j) & 255))
                self.strip.show()
                time.sleep(wait_ms/1000.0)

    def rainbow_cycle(self, wait_ms=20) -> None:
        """Draw rainbow that uniformly distributes itself across all pixels."""
        while self.executing:
            for j in range(255):
                for i in range(self.strip.numPixels()):
                    self.strip.setPixelColor(
                        i, self.wheel((int(i * 256 / self.strip.numPixels()) + j) & 255))
                self.strip.show()
                time.sleep(wait_ms/1000.0)

    def theater_chase_rainbow(self, wait_ms=50) -> None:
        """Rainbow movie theater light style chaser animation."""
        while self.executing:
            for j in range(255):
                for q in range(3):
                    for i in range(0, self.strip.numPixels(), 3):
                        self.strip.setPixelColor(i+q, self.wheel((i+j) % 255))
                    self.strip.show()
                    time.sleep(wait_ms/1000.0)
                    for i in range(0, self.strip.numPixels(), 3):
                        self.strip.setPixelColor(i+q, 0)
