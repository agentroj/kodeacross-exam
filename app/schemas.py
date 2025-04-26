# app/schemas.py
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from uuid import UUID


class CustomerBase(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., ge=0, example=30)
    contact_info: Optional[str] = Field(None, example="john.doe@example.com")
    is_disabled: bool = Field(False, example=False)
    medical_conditions: List[str] = Field(default=[], example=["diabetes"])


class CustomerCreate(CustomerBase):
    """Payload when creating a new customer."""


class Customer(CustomerBase):
    """Response model for a customer record."""
    id: UUID
    model_config = ConfigDict(from_attributes=True)


class RentalBase(BaseModel):
    customer_id: UUID
    shoe_size: float = Field(..., example=9.5)
    rental_fee: float = Field(..., gt=0, example=5.0)


class RentalCreate(RentalBase):
    """Payload when creating a new rental."""


class Rental(RentalBase):
    """Response model for a rental record."""
    id: UUID
    rental_date: str
    discount: float
    total_fee: float
    model_config = ConfigDict(from_attributes=True)
