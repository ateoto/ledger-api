import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


cwd = Path(__file__).resolve().parent

env_file = Path(cwd.parent.parent, "local.env")

with env_file.open() as env_file_obj:
    for line in env_file_obj:
        key, value = line.split(":")
        os.environ[key.strip()] = value.strip()


pg_user = os.getenv("POSTGRES_USER")
pg_pass = os.getenv("POSTGRES_PASSWORD")
pg_db = os.getenv("POSTGRES_DB")
pg_host = os.getenv("POSTGRES_HOST", "localhost")

SQLALCHEMY_DATABASE_URL = f"postgresql://{pg_user}:{pg_pass}@{pg_host}:5432/{pg_db}"


print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
