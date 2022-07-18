from pydantic import Field
from objectid import PydanticObjectId


class LightingRequest:
    def __init__(
        self,
        operation: str,
        h: int = 0,
        s: int = 100,
        v: int = 50,
        id: PydanticObjectId = Field(None, alias="_id"),
        brightness: int = None,
        temperature: int = None,
    ):
        self.id = id
        self.operation = operation
        self.brightness = brightness
        self.h = h
        self.s = s
        self.v = v
        self.temperature = temperature
