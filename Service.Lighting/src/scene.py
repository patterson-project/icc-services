from objectid import PydanticObjectId
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional
from lightingrequest import LightingRequest


class Scene(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    name: str
    requests: list[LightingRequest]

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data
