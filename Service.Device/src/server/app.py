from fastapi import FastAPI
from routes.devices import router as DeviceRouter

app = FastAPI(
    title="Devices API",
    description="API to perform CRUD operations on ICC devices",
    docs_url="/devices/docs",
    openapi_url="/devices/docs/openapi.json"
)


app.include_router(DeviceRouter, tags=[
                   "Devices"], prefix="/devices")


@app.get("/scenes/healthz", tags=["Health"])
async def health():
    return "Healthy"
