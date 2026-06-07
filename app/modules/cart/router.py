from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.core.dependencies import get_current_user

from app.modules.cart.schemas import (
    CartCreate,
    CartResponse
)

from app.modules.cart.service import (
    get_cart_items,
    add_to_cart,
    delete_cart_item
)

from app.db.models import Cart

router = APIRouter()


@router.get("/", response_model=list[CartResponse])
def get_my_cart(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_cart_items(
        int(user),
        db
    )


@router.post("/")
def add_item_to_cart(
    item: CartCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return add_to_cart(
        int(user),
        item.product_id,
        item.quantity,
        db
    )

@router.delete("/{cart_id}")
def remove_cart_item(
    cart_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    cart_item = (
    db.query(Cart)
    .filter(
        Cart.id == cart_id,
        Cart.user_id == int(user)
    )
    .first()
)

    if not cart_item:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    delete_cart_item(
        cart_item,
        db
    )

    return {
        "message": "Item removed from cart"
    }