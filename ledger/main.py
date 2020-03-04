from typing import List
from datetime import date, datetime
import csv
import os

from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from sqlalchemy.orm import Session

from . import crud, models, schemas
from ledger.db.session import scoped_session, db_session


app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_name(db, category_name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return crud.create_category(db=db, category=category)


@app.get("/categories/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories


@app.get("/categories/{category_slug}", response_model=schemas.Category)
def read_category(category_slug: str, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_slug(db, category_slug=category_slug)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@app.post("/vendors/", response_model=schemas.Vendor)
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
    db_vendor = crud.get_vendor_by_name(db, vendor_name=vendor.name)
    if db_vendor:
        raise HTTPException(status_code=400, detail="Vendor already exists")
    return crud.create_vendor(db=db, vendor=vendor)


@app.get("/vendors/", response_model=List[schemas.Vendor])
def read_vendors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vendors = crud.get_vendors(db, skip=skip, limit=limit)
    return vendors


@app.get("/vendors/{vendor_slug}", response_model=schemas.Vendor)
def read_vendor_slug(vendor_slug: str, db: Session = Depends(get_db)):
    db_vendor = crud.get_vendor_by_slug(db, vendor_slug=vendor_slug)
    if db_vendor is None:
        raise HTTPException(status_code=404, detail="Vendor not found")
    return db_vendor


@app.get("/transactions/", response_model=List[schemas.Transaction])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = crud.get_transactions(db, skip=skip, limit=limit)
    return transactions


@app.get("/transactions/{year}/{month}", response_model=List[schemas.Transaction])
def read_transactions_month(skip: int = 0, limit: int = 100, year: int = date.today().year, month: int = date.today().month, db: Session = Depends(get_db)):
    search_date = date(year, month, 1)
    transactions = crud.get_transactions_month(db, skip=skip, limit=limit, search_date=search_date)
    return transactions


@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transaction=transaction)


@app.post("/transactions/parse")
def parse_transactions_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    with open(file.filename, "wb") as uploaded_file:
        contents = file.file.read()
        uploaded_file.write(contents)

    with open(file.filename) as csv_file:
        tx_reader = csv.reader(csv_file)
        for line in tx_reader:
            print(f"{line}")
            #is_credit = line[4] == 'Sale'
            #if is_credit:
               # date_str = line[0]
               # vendor_str = line[2]
               # amount_usd = line[5]
               # category_str = line[3]

                #db_category = crud.get_or_create_category_by_name(db, category_name=category_str)
               # db_vendor = crud.get_or_create_vendor_by_name(db, vendor_name=vendor_str)

                #db_vendor.category_id = db_category.id


           # if db_vendor:
            #transaction = schemas.TransactionCreate()
            #transaction.date = datetime.strptime("%m/%d/%Y", date_str).date()
            #transaction
            #crud.create_transaction(db, transaction=transaction)

    os.remove(file.filename)
