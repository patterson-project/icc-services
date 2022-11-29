from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from server.database import RoomRepository
from icc.models import RoomDto, PydanticObjectId
from httpx import AsyncClient

router = APIRouter()
room_repository = RoomRepository()
http_client = AsyncClient()


@router.post("", summary="Create a room", response_description="The created room")
async def create_room(room: RoomDto):
    await room_repository.insert(room)
    return room.to_json()


@router.get("", summary="Get all rooms", response_description="List of all rooms")
async def get_all_rooms():
    print("IN GETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT\n\n\n\n\n")
    rooms = await room_repository.find_all()
    return jsonable_encoder(rooms)


@router.put("/{id}", summary="Update a room", response_description="Updated room object")
async def update_room(id: PydanticObjectId, room: RoomDto):
    updated_room = await room_repository.update(id, room)

    return jsonable_encoder(updated_room)


@router.delete("/{id}", summary="Delete a room", response_description="Deleted room")
async def delete_room(id: PydanticObjectId):
    deleted_room = await room_repository.delete(id)
    return jsonable_encoder(deleted_room)
