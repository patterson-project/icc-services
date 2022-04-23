from rpi_ws281x import Color
import time


class LedStripSequence:
    def wheel(self, pos) -> None:
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(self, strip, wait_ms=20) -> None:
        while True:
            for j in range(255):
                for i in range(strip.numPixels()):
                    strip.setPixelColor(i, self.wheel((i + j) & 255))
                strip.show()
                time.sleep(wait_ms / 1000.0)

    def rainbow_cycle(self, strip, wait_ms=20) -> None:
        while True:
            for j in range(255):
                for i in range(strip.numPixels()):
                    strip.setPixelColor(
                        i, self.wheel((int(i * 256 / strip.numPixels()) + j) & 255)
                    )
                strip.show()
                time.sleep(wait_ms / 1000.0)
