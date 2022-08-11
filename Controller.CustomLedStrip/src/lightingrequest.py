from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from objectid import PydanticObjectId
from fastapi.encoders import jsonable_encoder


class LightingRequest(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    target: PydanticObjectId
    operation: str
    h: int = 0
    s: int = 100
    v: int = 50
    brightness: int = None
    temperature: int = None
    date: datetime = datetime.utcnow()

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data
