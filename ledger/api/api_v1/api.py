from fastapi import APIRouter

from ledger.api.api_v1.endpoints import categories

api_router = APIRouter()
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
