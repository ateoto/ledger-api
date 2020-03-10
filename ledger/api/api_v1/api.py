from fastapi import APIRouter

from ledger.api.api_v1.endpoints import categories, users

api_router = APIRouter()
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(users.router, prefix="/users", tags=["users"])