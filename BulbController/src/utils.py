from datetime import datetime, timezone


class BulbRequest:
    def __init__(
        self,
        operation: str,
        h: int = 0,
        s: int = 100,
        v: int = 50,
        brightness: int = None,
        temperature: int = None,
    ):
        self.operation = operation
        self.brightness = brightness
        self.h = h
        self.s = s
        self.v = v
        self.temperature = temperature


def log(message):
    now = datetime.now(timezone.utc).astimezone().isoformat()
    print("[" + now + "]\t", end="")
    print(message)
