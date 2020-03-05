from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ledger import crud
from ledger.api.utils.db import get_db

from ledger.schemas.category import Category

router = APIRouter()


@router.get("/", response_model=List[Category])
def read_items(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
):
    categories = crud.category.get_multi(db, skip=skip, limit=limit)
    return categories
