from datetime import datetime


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


def log(message):
    now = datetime.now()
    print(str(now.strftime("%Y-%m-%d %H:%M:%S")), end="")
    print(message)
