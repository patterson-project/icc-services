import datetime


class LightingRequest:
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


class ServiceUris:
    DEVICE_DB = "localhost:27017"
    LED_STRIP_SERVICE = "http://10.0.0.68:8000"
    BULB_SERVICE = "http://bulb-controller-cluster-ip.default.svc.cluster.local:8000"


def log(message):
    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    print("[" + str(now.strftime("%Y-%m-%d %H:%M:%S")) + "]\t", end="")
    print(message)
