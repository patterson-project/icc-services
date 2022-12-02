from fastapi import FastAPI
from routes.lighting import router as LightingRouter

app = FastAPI(
    title="Lighting API",
    description="API to submit lighting requests",
    docs_url="/lighting/docs",
    openapi_url="/lighting/docs/openapi.json"
)

app.include_router(LightingRouter, tags=[
                   "Lighting Requests"], prefix="/lighting")


@app.get("/scenes/healthz", tags=["Health"])
async def health():
    return "Healthy"
