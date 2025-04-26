# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas


def create_customer(db: Session, data: schemas.CustomerCreate) -> models.Customer: # noqa
    cust = models.Customer(**data.dict())
    db.add(cust)
    db.commit()
    db.refresh(cust)
    return cust


def get_customers(db: Session):
    return db.query(models.Customer).all()


def create_rental(db: Session, data: schemas.RentalCreate, discount: float, total_fee: float): # noqa
    rent = models.Rental(**data.dict(), discount=discount, total_fee=total_fee)
    db.add(rent)
    db.commit()
    db.refresh(rent)
    return rent


def get_rentals(db: Session):
    return db.query(models.Rental).all()
