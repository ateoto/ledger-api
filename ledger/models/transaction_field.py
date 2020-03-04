from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ledger.db.base_class import Base


class TransactionField(Base):
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)


class TransactionFieldMapping(Base):
    id = Column(Integer, primary_key=True, unique=True)
    transaction_field_id = Column(Integer, ForeignKey("transaction_fields.id"))
    mapping = Column(String)
    implies_tx_type = Column(Boolean)
    transaction_field = relationship("TransactionField")
