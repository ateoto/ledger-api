from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ledger import crud
from ledger.api.utils.db import get_db

from ledger.schemas.user import User

router = APIRouter()


@router.get("/")
def read_item():
    return {"Not": "Implemented"}
