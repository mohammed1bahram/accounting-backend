from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import customer, vendor
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(
    title="Accountant's Blueprint API",
    description="Accounting & Management API (multi-language ready)",
    version="1.0.0"
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in prod!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session (future login support)
app.add_middleware(SessionMiddleware, secret_key="supersecret-key")

# Routers
app.include_router(customer.router)
app.include_router(vendor.router)

@app.get("/")
def root():
    return {"msg": "Welcome to Accountant's Blueprint API"}