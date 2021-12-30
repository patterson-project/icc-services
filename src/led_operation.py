import time
from rpi_ws281x import Color
from utils import bcolors


class LedOperation:
    def __init__(self, operation_name) -> None:
        self.operation_name = operation_name
        self.running = True
        self.operation_names = {'colorWipe': self.colorWipe, 'theaterChase': self.theaterChase, 'rainbow': self.rainbow,
                                'rainbowCycle': self.rainbowCycle, 'theaterChaseRainbow': self.theaterChaseRainbow}

    def run(self) -> None:
        try:
            self.operation_names[self.operation_name]()
        except KeyError as e:
            print(f"{bcolors.WARNING}ERROR:\n {e.message}{bcolors.ENDC}")

    def terminate(self) -> None:
        self.running = False

    def colorWipe(self, strip, colors=[Color(255, 0, 0), Color(0, 255, 0), Color(0, 0, 255)], wait_ms=50):
        while self.executing:
            for color in colors:
                self.wipe(strip, color, wait_ms)

    def wipe(self, strip, color, wait_ms=50) -> None:
        """Wipe color across display a pixel at a time."""
        while self.executing:
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
                strip.show()
                time.sleep(wait_ms/1000.0)

    def theaterChase(self, strip, color=Color(127, 127, 127), wait_ms=50) -> None:
        """Movie theater light style chaser animation."""
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

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

    def rainbow(self, strip, wait_ms=20) -> None:
        """Draw rainbow that fades across all pixels at once."""
        while self.executing:
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((i+j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)

    def rainbowCycle(self, strip, wait_ms=20) -> None:
        """Draw rainbow that uniformly distributes itself across all pixels."""
        while self.executing:
            for i in range(strip.numPixels()):
                strip.setPixelColor(
                    i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)

    def theaterChaseRainbow(self, strip, wait_ms=50) -> None:
        """Rainbow movie theater light style chaser animation."""
        while self.executing:
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, self.wheel((i+j) % 255))
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)
