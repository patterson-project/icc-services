from fastapi import FastAPI
from routes.devices import router as DeviceRouter
from routes.rooms import router as RoomRouter

app = FastAPI(
    title="Devices API",
    description="API to perform CRUD operations on ICC devices",
    docs_url="/devices/docs",
    openapi_url="/devices/docs/openapi.json"
)


@app.get("/scenes/healthz", tags=["Health"])
async def health():
    return "Healthy"

app.include_router(DeviceRouter, tags=[
                   "Devices"], prefix="/devices")
app.include_router(RoomRouter, tags=[
                   "Rooms"], prefix="/devices/rooms")
