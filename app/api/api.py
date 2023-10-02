from fastapi import APIRouter
from app.api.endpoints import (bus)

api_router = APIRouter()

api_router.include_router(bus.router, tags=['Bus basic api'])