from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from server.database import SceneRepository
from icc.models import SceneDto, PydanticObjectId

router = APIRouter()
scene_repository = SceneRepository()


@router.post("", tags=["Scenes"], summary="Create a scene", response_description="The created scene")
async def create_scene(scene: SceneDto):
    await scene_repository.insert(scene)
    return scene.to_json()


@router.get("", summary="Get all scenes", response_description="List of scenes")
async def get_all_scenes():
    scenes = await scene_repository.find_all()
    return jsonable_encoder(scenes)


@router.put("/{id}", summary="Update a scene", response_description="Updated scene object")
async def update_scene(id: PydanticObjectId, scene: SceneDto):
    updated_scene = await scene_repository.update(id, scene)
    return jsonable_encoder(updated_scene)


@router.delete("/{id}", summary="Delete a scene", response_description="Deleted Object")
async def update_scene(id: PydanticObjectId):
    deleted_scene = await scene_repository.delete(id)
    return jsonable_encoder(deleted_scene)
