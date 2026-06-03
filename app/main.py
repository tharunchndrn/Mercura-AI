from fastapi import FastAPI
from app.modules.products.router import router as products_router

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