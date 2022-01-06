from datetime import datetime


class TerminalColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class LedConfig:
    COUNT = 88
    PIN = 18
    FREQ_HZ = 800000
    DMA = 10
    BRIGHTNESS = 255
    INVERT = False
    CHANNEL = 0
    BROKER_ADDRESS = "10.0.0.35"


class LedRequest:
    def __init__(self, operation: str, r: int = None, g: int = None, b: int = None):
        self.operation = operation
        self.r = r
        self.g = g
        self.b = b


def log(topic, message):
    now = datetime.now()
    print(str(now.strftime('%Y-%m-%d %H:%M:%S')))
    print("\tTOPIC:\t\t" + topic)
    print("\tMESSAGE:\t" + message)
