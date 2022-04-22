from datetime import datetime


class LedConfig:
    COUNT = 100
    PIN = 18
    FREQ_HZ = 800000
    DMA = 10
    BRIGHTNESS = 255
    INVERT = False
    CHANNEL = 0
    BROKER_ADDRESS = "10.0.0.35"


def log(message):
    now = datetime.now()
    print(str(now.strftime("%Y-%m-%d %H:%M:%S")), end="")
    print(message)


class LedRequest:
    def __init__(
        self,
        operation: str,
        h: int = None,
        s: int = None,
        l: int = None,
        a: int = None,
        brightness: int = None,
        wait_ms: int = None,
    ):
        self.operation = operation
        self.brightness = brightness
        self.h = h
        self.s = s
        self.l = l
        self.a = a
        self.wait_ms = wait_ms
