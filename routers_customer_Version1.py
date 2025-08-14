from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas import CustomerCreate, CustomerOut
import models

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/", response_model=list[CustomerOut])
def list_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

@router.post("/", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer