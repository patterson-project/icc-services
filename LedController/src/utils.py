from datetime import datetime


class LedStripConfig:
    COUNT = 100
    PIN = 18
    FREQ_HZ = 800000
    DMA = 10
    BRIGHTNESS = 255
    INVERT = False
    CHANNEL = 0


class LightingRequest:
    def __init__(
        self,
        operation: str,
        h: int = 0,
        s: int = 100,
        v: int = 50,
        brightness: int = None,
        delay: int = None,
    ):
        self.operation = operation
        self.brightness = brightness
        self.h = h
        self.s = s
        self.v = v
        self.delay = delay


def log(topic, message):
    now = datetime.now()
    print(str(now.strftime("%Y-%m-%d %H:%M:%S")))
    print("\tTOPIC:\t\t" + topic)
    print("\tMESSAGE:\t" + message)
