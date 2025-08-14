from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
import uuid

Base = declarative_base()

def gen_uuid():
    return str(uuid.uuid4())

class Customer(Base):
    __tablename__ = "customer"
    id = Column(String, primary_key=True, default=gen_uuid)
    code = Column(String(30), unique=True, nullable=False)
    name = Column(String(150), nullable=False)
    currency_id = Column(String, nullable=True)
    terms_days = Column(Integer, default=0)
    credit_limit = Column(Numeric(18,2), default=0)
    receivable_account_id = Column(String, nullable=True)
    tax_code_id = Column(String, nullable=True)

class Vendor(Base):
    __tablename__ = "vendor"
    id = Column(String, primary_key=True, default=gen_uuid)
    code = Column(String(30), unique=True, nullable=False)
    name = Column(String(150), nullable=False)
    currency_id = Column(String, nullable=True)
    terms_days = Column(Integer, default=0)
    credit_limit = Column(Numeric(18,2), default=0)
    payable_account_id = Column(String, nullable=True)
    tax_code_id = Column(String, nullable=True)