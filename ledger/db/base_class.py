from sqlalchemy.ext.declarative import declarative_base, declared_attr
from slugify import slugify
from inflection import tableize


class CustomBase(object):
    @declared_attr
    def __tablename__(cls):
        return tableize(cls.__name__)


class SlugBase(CustomBase):
    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)


Base = declarative_base(cls=CustomBase)
