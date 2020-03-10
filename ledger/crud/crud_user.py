from ledger.models.user import User
from ledger.schemas.user import UserCreate, UserUpdate
from ledger.crud.base import CRUDBase


class CRUDCategory(CRUDBase[User, UserCreate, UserUpdate]):
    pass


user = CRUDCategory(User)
