from datetime import datetime, timezone


class LightingRequest:
    def __init__(
        self,
        operation: str,
        h: int = 0,
        s: int = 100,
        v: int = 50,
        brightness: int = None,
        temperature: int = None,
        scene: str = None,
    ):
        self.operation = operation
        self.brightness = brightness
        self.h = h
        self.s = s
        self.v = v
        self.temperature = temperature
        self.scene = scene


class ServiceUris:
    MONGO_DB = "10.0.0.34:27017"
