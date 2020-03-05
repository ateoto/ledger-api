from ledger.models.transaction import Transaction
from ledger.schemas.transaction import TransactionCreate
from ledger.crud.base import CRUDBase


class CRUDTransaction(CRUDBase[Transaction, TransactionCreate]):
    pass


transaction = CRUDTransaction(Transaction)
