from pydantic import BaseModel

class CustomerCreate(BaseModel):
    code: str
    name: str
    currency_id: str | None = None
    terms_days: int = 0
    credit_limit: float = 0
    receivable_account_id: str | None = None
    tax_code_id: str | None = None

class CustomerOut(CustomerCreate):
    id: str

class VendorCreate(BaseModel):
    code: str
    name: str
    currency_id: str | None = None
    terms_days: int = 0
    credit_limit: float = 0
    payable_account_id: str | None = None
    tax_code_id: str | None = None

class VendorOut(VendorCreate):
    id: str