from pydantic import BaseModel


class VendorBase(BaseModel):
    name: str


class VendorCreate(VendorBase):
    pass


class VendorUpdate(VendorBase):
    pass


class Vendor(VendorBase):
    id: int
    category_id: int

    class Config:
        orm_mode = True
