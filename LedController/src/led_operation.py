from rpi_ws281x import Color
import time
from kasa import SmartBulb
import asyncio
import colorsys


def off(strip) -> None:
    for i in range(strip.numPixels()):
        strip.setPixelColorRGB(i, 0, 0, 0)
        strip.show()


async def rgb(strip, bulb_1, bulb_2, r, g, b, wait_ms=5) -> None:
    await set_bulb_color(bulb_1, r, g, b)
    await set_bulb_color(bulb_2, r, g, b)

    for i in range(strip.numPixels()):
        strip.setPixelColorRGB(i, r, b, g)
        strip.show()
        time.sleep(wait_ms/1000.0)


async def set_bulb_color(bulb, r, g, b) -> None:
    h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    h = int(360 * h)
    s = int(100 * s)
    v = int(100 * v)

    asyncio.run(bulb.set_hsv(h, s, v))
    asyncio.run(bulb.update())


def sunrise(strip) -> None:
    strip.setBrightness(0)
    strip.show()

    for i in range(strip.numPixels()):
        strip.setPixelColorRGB(i, 253, 211, 251)
    strip.show()

    for i in range(256):
        strip.setBrightness(i)
        strip.show()
        time.sleep(1)


def brightness(strip, brightness) -> None:
    strip.setBrightness(int(255*(brightness/100)))
    strip.show()


def color_wipe(strip, colors=[Color(255, 0, 0), Color(0, 255, 0), Color(0, 0, 255)], wait_ms=50):
    while True:
        for color in colors:
            wipe(strip, color, wait_ms)


def wipe(strip, color, wait_ms=50) -> None:
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def theater_chase(strip, color=Color(127, 127, 127), wait_ms=50) -> None:
    """Movie theater light style chaser animation."""
    while True:
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)


def wheel(pos) -> None:
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20) -> None:
    """Draw rainbow that fades across all pixels at once."""
    while True:
        for j in range(255):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, wheel((i+j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)


def rainbow_cycle(strip, wait_ms=20) -> None:
    """Draw rainbow that uniformly distributes itself across all pixels."""
    while True:
        for j in range(255):
            for i in range(strip.numPixels()):
                strip.setPixelColor(
                    i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)


def theater_chase_rainbow(strip, wait_ms=50) -> None:
    """Rainbow movie theater light style chaser animation."""
    while True:
        for j in range(255):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, wheel((i+j) % 255))
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)
