from typing import Union
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app.api.api import api_router
from app.core.config import settings


app = FastAPI(
    title= "customize_bus_data"
)

if settings.BACKEND_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_ORIGINS.split(','),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
