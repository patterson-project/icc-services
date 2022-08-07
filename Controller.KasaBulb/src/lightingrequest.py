from typing import Optional
from pydantic import BaseModel, Field
from objectid import PydanticObjectId


class LightingRequest(BaseModel):
    target: PydanticObjectId
    operation: str
    h: int = 0
    s: int = 100
    v: int = 50
    brightness: int = None
    temperature: int = None
