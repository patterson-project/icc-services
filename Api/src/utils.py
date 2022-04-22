from datetime import datetime


def log(message):
    now = datetime.now()
    print(str(now.strftime("%Y-%m-%d %H:%M:%S")), end="")
    print(message)


class LedRequest:
    def __init__(
        self,
        operation: str,
        h: int = 0,
        s: int = 100,
        v: int = 50,
        brightness: int = None,
        wait_ms: int = None,
    ):
        self.operation = operation
        self.brightness = brightness
        self.h = h
        self.s = s
        self.v = v
        self.wait_ms = wait_ms
