from fastapi import FastAPI
from routes.scene import router as SceneRouter
from routes.scenerequest import router as SceneRequestRouter

app = FastAPI(
    title="Scenes API",
    description="API to perform CRUD operations on ICC scenes"
)


@app.get("/healthz", tags=["Health"])
async def health():
    return "Healthy"

app.include_router(SceneRequestRouter, tags=[
                   "Scene Requests"], prefix="/scene/request")
app.include_router(SceneRouter, tags=["Scenes"], prefix="/scene")