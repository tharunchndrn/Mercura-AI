from fastapi import FastAPI
from app.modules.products.router import router as products_router

from app.db.database import engine, Base 
from app.db.models import Product

from app.modules.orders.router import (
    router as orders_router
)

from app.modules.users.router import (
    router as users_router
)

from app.modules.auth.router import (
    router as auth_router
)

from app.modules.cart.router import (
    router as cart_router
)

from app.modules.payments.router import (
    router as payments_router
)

app = FastAPI(
    title="Autonomous Ecommerce AI Agent",
    description="Backend API for AI-Powered Ecommerce System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Backend Running Successfully"
    }

app.include_router(
    products_router,
    prefix="/products",
    tags=["Products"]
)

app.include_router(
    orders_router,
    prefix="/orders",
    tags=["Orders"]
)

app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    cart_router,
    prefix="/cart",
    tags=["Cart"]
)

app.include_router(
    payments_router,
    prefix="/payments",
    tags=["Payments"]
)