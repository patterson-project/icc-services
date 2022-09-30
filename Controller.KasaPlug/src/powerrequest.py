from typing import Optional
from pydantic import BaseModel, Field
from objectid import PydanticObjectId


class PowerRequest(BaseModel):
    target: PydanticObjectId
    operation: str
