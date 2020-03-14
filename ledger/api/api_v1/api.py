from fastapi import APIRouter, Depends

from ledger.schemas.JWT import JWTBearer
from ledger.api.utils.auth import jwks
from ledger.api.api_v1.endpoints import categories, users, auth


jwt_auth = JWTBearer(jwks)

api_router = APIRouter()

api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(users.router, prefix="/users", dependencies=[Depends(jwt_auth)], tags=["users"])
api_router.include_router(auth.router, prefix="/auth")
