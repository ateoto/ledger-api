from pydantic import BaseModel


class TransactionFieldBase(BaseModel):
    name: str = None


class TransactionFieldCreate(TransactionFieldBase):
    pass


class TransactionField(TransactionFieldBase):
    pass


class TransactionFieldMappingBase(BaseModel):
    mapping: str = None
    implies_tx_type: bool = False


class TransactionFieldMappingCreate(TransactionFieldMappingBase):
    pass


class TransactionFieldMapping(TransactionFieldMappingBase):
    pass