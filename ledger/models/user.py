from sqlalchemy import Column, Integer, String

from ledger.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String)
