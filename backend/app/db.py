import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql+psycopg://app:app@localhost:5432/appdb")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass
