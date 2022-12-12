from fastapi import FastAPI
from routes.request import router as KasaPlugRequestRouter

app = FastAPI(
    title="Kasa Plug API",
    description="API to make Kasa Plug power requests",
    docs_url="/docs",
    openapi_url="/docs/openapi.json",
)

app.include_router(
    KasaPlugRequestRouter, tags=["Kasa Plug Requests"]
)


@app.get("/healthz", tags=["Health"])
async def health():
    return "Healthy"
