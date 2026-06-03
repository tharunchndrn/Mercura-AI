from fastapi import APIRouter
from app.modules.products.schemas import Product

router = APIRouter()

products = [
    Product(
        id=1,
        name="Nike Air Max",
        price=120
    ),
    Product(
        id=2,
        name="Adidas Ultraboost",
        price=150
    ),
    Product(
        id=3,
        name="Puma Runner",
        price=100
    )
]

@router.get("/")
def get_products():
    return products


@router.get("/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product

    return {"error": "Product not found"}

@router.post("/")
def create_product(product: Product):
    products.append(product)

    return {
        "message": "Product created successfully",
        "product": product
    }