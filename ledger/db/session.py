from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://ledgerdb:ledgerdbpass@localhost:5432/ledger"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
