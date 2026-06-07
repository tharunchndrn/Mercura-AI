from sqlalchemy.orm import Session

from app.db.models import (
    Order,
    Product
)


def get_all_orders(db: Session):
    return db.query(Order).all()


def get_order_by_id(
    order_id: int,
    db: Session
):
    return (
        db.query(Order)
        .filter(Order.id == order_id)
        .first()
    )


def create_order(
    user_id: int,
    product_id: int,
    quantity: int,
    db: Session
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        return None

    if product.stock < quantity:
        return "OUT_OF_STOCK"

    order = Order(
    user_id=user_id,
    product_id=product_id,
    quantity=quantity
)

    product.stock -= quantity

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def delete_order(
    order: Order,
    db: Session
):
    product = (
        db.query(Product)
        .filter(Product.id == order.product_id)
        .first()
    )

    if product:
        product.stock += order.quantity

    db.delete(order)
    db.commit()