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
        l: int = 50,
        a: int = 1,
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
