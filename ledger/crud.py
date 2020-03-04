from datetime import date
from calendar import monthrange
from sqlalchemy.orm import Session

from . import models, schemas


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_category_by_name(db: Session, category_name: str):
    return db.query(models.Category).filter(models.Category.name == category_name).first()


def get_category_by_slug(db: Session, category_slug: str):
    return db.query(models.Category).filter(models.Category.slug == category_slug).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_or_create_category_by_name(db: Session, category_name: str):
    db_category = get_category_by_name(db, category_name=category_name)
    if db_category is None:
        category = schemas.CategoryCreate()
        category.name = category_name
        db_category = create_category(db, category=category)
    return db_category


def get_vendor(db: Session, vendor_id: int):
    return db.query(models.Vendor).filter(models.Vendor.id == vendor_id).first()


def get_vendor_by_name(db: Session, vendor_name):
    return db.query(models.Vendor).filter(models.Vendor.name == vendor_name).first()


def get_vendor_by_slug(db: Session, vendor_slug):
    return db.query(models.Vendor).filter(models.Vendor.slug == vendor_slug).first()


def get_vendors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vendor).offset(skip).limit(limit).all()


def create_vendor(db: Session, vendor: schemas.VendorCreate):
    db_vendor = models.Vendor(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor


def get_or_create_vendor_by_name(db: Session, vendor_name: str):
    db_vendor = get_vendor_by_name(db, vendor_name=vendor_name)
    if db_vendor is None:
        # Search Aliases for a match.
        vendor = schemas.VendorCreate()
        vendor.name = vendor_name
        db_vendor = create_vendor(db, vendor)
    return db_vendor


def update_vendor(db: Session, vendor: schemas.Vendor):
    db_vendor = models.Vendor(**vendor.dict())
    


def get_transaction(db: Session, transaction_id: int):
    return db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()


def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Transaction).offset(skip).limit(limit).all()


def get_transactions_month(db: Session, skip: int = 0, limit: int = 100, search_date: date = date.today()):
    start_date = date(search_date.year, search_date.month, 1)
    _, days_in_month = monthrange(search_date.year, search_date.month)
    end_date = date(search_date.year, search_date.month, days_in_month)
    return db.query(models.Transaction).offset(skip).limit(limit)\
        .filter(models.Transaction.date >= start_date)\
        .filter(models.Transaction.date <= end_date)


def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_category = get_category_by_name(db, transaction.category)
    if db_category is None:
        category = schemas.CategoryCreate()
        category.name = transaction.category
        db_category = create_category(db, category)

    db_vendor = get_vendor_by_name(db, transaction.vendor)
    if db_vendor is None:
        vendor = schemas.VendorCreate()
        vendor.name = transaction.vendor
        vendor.category_id = db_category.id
        db_vendor = create_vendor(db, vendor)

    db_transaction = models.Transaction(**transaction.dict())
    db_transaction.vendor_id = db_vendor.id
    db_transaction.category_id = db_category.id

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
