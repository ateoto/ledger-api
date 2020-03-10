from pydantic import BaseModel


class UserBase(BaseModel):
    email: str = None


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
