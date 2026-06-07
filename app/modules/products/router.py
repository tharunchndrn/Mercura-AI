from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.modules.products.schemas import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from app.modules.products.service import (
    get_all_products,
    get_product_by_id,
    create_product as create_product_service,
    update_product as update_product_service,
    delete_product as delete_product_service
)

from app.core.dependencies import (
    get_current_user
)

router = APIRouter()


@router.get("/", response_model=list[ProductResponse])
def get_products(
    db: Session = Depends(get_db)
):
    return get_all_products(db)


@router.get("/{product_id}",
            response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = get_product_by_id(product_id, db)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


@router.post("/")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_product_service(
        product.name,
        product.price,
        product.stock,
        db
    )

@router.put("/{product_id}",
            response_model=ProductResponse)
def update_product(
    product_id: int,
    updated_product: ProductUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    product = get_product_by_id(
        product_id,
        db
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return update_product_service(
        product,
        updated_product.name,
        updated_product.price,
        updated_product.stock,
        db
    )

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    product = get_product_by_id(product_id, db)

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    delete_product_service(product, db)

    return {
        "message": "Product deleted successfully"
    }