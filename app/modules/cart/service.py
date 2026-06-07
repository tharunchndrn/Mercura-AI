from sqlalchemy.orm import Session
from app.db.models import Cart


def get_cart_items(user_id: int, db: Session):
    return (
        db.query(Cart)
        .filter(Cart.user_id == user_id)
        .all()
    )


def add_to_cart(
    user_id: int,
    product_id: int,
    quantity: int,
    db: Session
):
    cart_item = Cart(
        user_id=user_id,
        product_id=product_id,
        quantity=quantity
    )

    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)

    return cart_item


def delete_cart_item(
    cart_item,
    db: Session
):
    db.delete(cart_item)
    db.commit()