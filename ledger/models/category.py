from sqlalchemy import Column, Integer, String, event

from ledger.db.base_class import SlugBase


class Category(SlugBase):
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String)
    slug = Column(String(100))


event.listen(Category.name, 'set', Category.generate_slug, retval=False)