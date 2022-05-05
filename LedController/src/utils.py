from datetime import datetime, timezone
from rpi_ws281x import Color


def wheel(pos) -> None:
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


class LedStripConfig:
    COUNT = 100
    PIN = 18
    FREQ_HZ = 800000
    DMA = 10
    BRIGHTNESS = 255
    INVERT = False
    CHANNEL = 0


class LedStripRequest:
    def __init__(
        self,
        operation: str,
        h: int = 0,
        s: int = 100,
        v: int = 50,
        brightness: int = None,
    ):
        self.operation = operation
        self.brightness = brightness
        self.h = h
        self.s = s
        self.v = v


def log(message):
    now = datetime.now(timezone.utc).astimezone().isoformat()
    print("[" + now + "]\t", end="")
    print(message)
