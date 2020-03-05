from ledger.models.vendor import Vendor
from ledger.schemas.vendor import VendorCreate, VendorUpdate
from ledger.crud.base import CRUDBase


class CRUDVendor(CRUDBase[Vendor, VendorCreate, VendorUpdate]):
    pass


vendor = CRUDVendor(Vendor)
