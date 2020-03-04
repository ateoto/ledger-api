from sqlalchemy import Date, Boolean, Column, ForeignKey, Integer, String, func, BigInteger
from sqlalchemy.orm import relationship

from ledger.db.base_class import Base


class Transaction(Base):
    id = Column(Integer, primary_key=True, unique=True)
    date = Column(Date, default=func.now(), nullable=False)
    amount = Column(BigInteger, nullable=False)
    is_credit = Column(Boolean, default=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    raw = Column(String)
    vendor = relationship("Vendor")
    category = relationship("Category")