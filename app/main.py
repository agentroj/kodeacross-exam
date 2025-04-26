# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, models
from .database import engine, get_db
from .llm import get_discount

# Create tables automatically on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bowling Shoe Rental – SQLite Edition",
    version="1.0"
)


@app.post("/customers", response_model=schemas.Customer)
def add_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)): # noqa
    return crud.create_customer(db, customer)


@app.get("/customers", response_model=list[schemas.Customer])
def list_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)


@app.post("/rentals", response_model=schemas.Rental)
async def add_rental(
    rental: schemas.RentalCreate,
    db: Session = Depends(get_db)
):
    # validate customer
    cust = db.get(models.Customer, str(rental.customer_id))
    if not cust:
        raise HTTPException(404, "Customer not found")

    # get discount via your llm.get_discount(...)
    discount_pct = await get_discount(cust)
    total = rental.rental_fee * (1 - discount_pct/100)

    return crud.create_rental(db, rental, discount_pct, total)


@app.get("/rentals", response_model=list[schemas.Rental])
def list_rentals(db: Session = Depends(get_db)):
    return crud.get_rentals(db)
