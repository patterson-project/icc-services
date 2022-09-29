from typing import Optional
from pydantic import BaseModel, Field
from objectid import PydanticObjectId


class PowerRequest(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    target: Optional[PydanticObjectId]
    name: Optional[str]
    operation: str
