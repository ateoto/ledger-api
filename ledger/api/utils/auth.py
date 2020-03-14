import os
from pathlib import Path
import requests

from fastapi import Depends, HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from ledger.schemas.JWT import JWKS, JWTBearer, JWTAuthorizationCredentials

cwd = Path(__file__).resolve().parent

env_file = Path(cwd.parent.parent.parent, "local.env")

with env_file.open() as env_file_obj:
    for line in env_file_obj:
        key, value = line.split(":")
        os.environ[key.strip()] = value.strip()


jwks = JWKS.parse_obj(
    requests.get(
        f"https://cognito-idp.{os.environ.get('COGNITO_REGION')}.amazonaws.com/"
        f"{os.environ.get('COGNITO_POOL_ID')}/.well-known/jwks.json"
    ).json()
)

auth = JWTBearer(jwks)


async def get_current_user(
        credentials: JWTAuthorizationCredentials = Depends(auth)
) -> str:
    try:
        return credentials.claims["username"]
    except KeyError:
        HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Username missing")