# app/models.py
import uuid
from sqlalchemy import Column, String, Integer, Boolean, Numeric, DateTime, ForeignKey, func # noqa
from sqlalchemy.dialects.sqlite import DATETIME
from sqlalchemy.types import JSON
from .database import Base


class Customer(Base):
    __tablename__ = "customers"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    contact_info = Column(String, nullable=True)
    is_disabled = Column(Boolean, default=False, nullable=False)
    medical_conditions = Column(JSON, default=list)  # JSON array for SQLite


class Rental(Base):
    __tablename__ = "rentals"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = Column(String, ForeignKey("customers.id"), nullable=False)
    rental_date = Column(DATETIME, server_default=func.datetime("now"))
    shoe_size = Column(Numeric, nullable=False)
    rental_fee = Column(Numeric, nullable=False)
    discount = Column(Numeric, nullable=False)
    total_fee = Column(Numeric, nullable=False)
