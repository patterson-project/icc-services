from datetime import datetime


def log(message):
    now = datetime.now()
    print(str(now.strftime('%Y-%m-%d %H:%M:%S')), end="")
    print(message)


class LedRequest:
    def __init__(self, operation: str, r: int = None, g: int = None, b: int = None):
        self.operation = operation
        self.r = r
        self.g = g
        self.b = b
