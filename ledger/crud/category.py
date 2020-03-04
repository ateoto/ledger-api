from ledger.models.category import Category
from ledger.schemas.category import CategoryCreate
from ledger.crud.base import CRUDBase


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
