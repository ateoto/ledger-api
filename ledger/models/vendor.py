from sqlalchemy import Column, ForeignKey, Integer, String, event
from sqlalchemy.orm import relationship

from ledger.db.base_class import Base, SlugBase


class Vendor(SlugBase):
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    slug = Column(String(100))
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category")


class VendorAlias(Base):
    alias = Column(String, primary_key=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"), primary_key=True)
    vendor = relationship("Vendor")


event.listen(Vendor.name, 'set', Vendor.generate_slug, retval=False)
