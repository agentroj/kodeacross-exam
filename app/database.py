# app/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

# will live as ./app.db inside the container
SQLITE_URL = os.getenv("SQLITE_URL", "sqlite:///./app.db")

# for sync usage:
engine = create_engine(
    SQLITE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# Base for your ORM models
Base = declarative_base()


def get_db():
    """Yield a SQLAlchemy Session, closing afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
