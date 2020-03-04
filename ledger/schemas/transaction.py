from datetime import date
from pydantic import BaseModel


class TransactionBase(BaseModel):
    date: date
    amount: int
    is_credit: bool
    raw: str


class TransactionCreate(TransactionBase):
    vendor: str
    category: str


class Transaction(TransactionBase):
    id: int
    vendor_id: int
    category_id: int

    class Config:
        orm_mode = True
