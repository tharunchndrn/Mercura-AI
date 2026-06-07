from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.modules.orders.schemas import (
    OrderCreate,
    OrderResponse
)

from app.modules.orders.service import (
    get_all_orders,
    get_order_by_id,
    create_order,
    delete_order
)

from app.core.dependencies import get_current_user
from app.db.models import Order

router = APIRouter()


@router.get("/", response_model=list[OrderResponse])
def get_orders(
    db: Session = Depends(get_db)
):
    return (
        db.query(Order)
        .filter(Order.user_id.isnot(None))
        .all()
    )


@router.get("/my-orders")
def get_my_orders(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return (
        db.query(Order)
        .filter(
            Order.user_id == int(user)
        )
        .all()
    )


@router.get("/{order_id}",
            response_model=OrderResponse)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    order = get_order_by_id(order_id, db)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    if order.user_id != int(user):
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return order


@router.post(
    "/",
    response_model=OrderResponse
)
def create_new_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    created_order = create_order(
        int(user),
        order.product_id,
        order.quantity,
        db
    )

    if not created_order:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    if created_order == "OUT_OF_STOCK":
        raise HTTPException(
            status_code=400,
            detail="Not enough stock available"
        )

    return created_order


@router.delete("/{order_id}")
def delete_existing_order(
    order_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    order = get_order_by_id(order_id, db)

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    if order.user_id != int(user):
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    delete_order(order, db)

    return {
        "message": "Order deleted successfully"
    }