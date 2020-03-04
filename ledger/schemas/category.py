from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
