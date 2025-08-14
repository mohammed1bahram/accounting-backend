from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas import VendorCreate, VendorOut
import models

router = APIRouter(prefix="/vendors", tags=["Vendors"])

@router.get("/", response_model=list[VendorOut])
def list_vendors(db: Session = Depends(get_db)):
    return db.query(models.Vendor).all()

@router.post("/", response_model=VendorOut)
def create_vendor(vendor: VendorCreate, db: Session = Depends(get_db)):
    db_vendor = models.Vendor(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor