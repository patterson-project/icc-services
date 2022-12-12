from fastapi import FastAPI
from routes.request import router as KasaLedStripRequestRouter

app = FastAPI(
    title="Kasa Led Strip API",
    description="API to make Kasa Led Strip lighting requests",
    docs_url="/docs",
    openapi_url="/docs/openapi.json",
)

app.include_router(
    KasaLedStripRequestRouter, tags=["Kasa Led Strip Requests"]
)


@app.get("/healthz", tags=["Health"])
async def health():
    return "Healthy"
