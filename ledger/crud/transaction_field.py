from ledger.models.transaction_field import  TransactionField, TransactionFieldMapping
from ledger.schemas.transaction_field import TransactionFieldCreate, TransactionFieldMappingCreate
from ledger.crud.base import CRUDBase


class CRUDTransactionField(CRUDBase[TransactionField, TransactionFieldCreate]):
    pass


class CRUDTransactionFieldMapping(CRUDBase[TransactionFieldMapping, TransactionFieldMappingCreate]):
    pass


transaction_field = CRUDTransactionField(TransactionField)
transaction_field_mapping = CRUDTransactionFieldMapping(TransactionFieldMapping)
