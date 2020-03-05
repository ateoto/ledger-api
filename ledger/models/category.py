from sqlalchemy import Column, Integer, String

from ledger.db.base_class import Base


class Category(Base):
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    slug = Column(String(100))
