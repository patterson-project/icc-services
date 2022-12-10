from fastapi import FastAPI
from routes.plugrequest import router as KasaPlugRequestRouter

app = FastAPI(
    title="Kasa Plug API",
    description="API to make Kasa Plug requests",
    docs_url="/docs",
    openapi_url="/docs/openapi.json",
)

app.include_router(
    KasaPlugRequestRouter, tags=["Kasa Plug Requests"], prefix="/request"
)


@app.get("/healthz", tags=["Health"])
async def health():
    return "Healthy"
