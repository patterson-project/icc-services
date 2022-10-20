from powerrequest import PowerRequest
from objectid import PydanticObjectId
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional
from lightingrequest import LightingRequest
from datetime import datetime


class Scene(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    name: str
    lighting_requests: Optional[list[LightingRequest]]
    power_requests: Optional[list[PowerRequest]]
    date: datetime = datetime.utcnow().isoformat()

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data


class SceneDto(BaseModel):
    name: str
    date: datetime = datetime.utcnow().isoformat()

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data
