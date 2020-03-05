from ledger.models.category import Category
from ledger.schemas.category import CategoryCreate, CategoryUpdate
from ledger.crud.base import CRUDBase


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    pass


category = CRUDCategory(Category)
