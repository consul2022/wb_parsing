from fastapi import FastAPI
from app.api.routers import routers as search_router


app = FastAPI(title="Parser WB")
app.include_router(search_router)


@app.get("/health")
def health():
    return {"status": "ok"}
