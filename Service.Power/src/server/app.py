from fastapi import FastAPI
from routes.power import router as PowerRouter

app = FastAPI(
    title="Power API",
    description="API to submit power requests",
    docs_url="/power/docs",
    openapi_url="/power/docs/openapi.json"
)

app.include_router(PowerRouter, tags=[
                   "Power Requests"], prefix="/power")


@app.get("/power/healthz", tags=["Health"])
async def health():
    return "Healthy"
