from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.db.models import Order

from app.modules.payments.schemas import (
    PaymentWebhook
)

router = APIRouter()


@router.post("/webhook")
def payment_webhook(
    payload: PaymentWebhook,
    db: Session = Depends(get_db)
):
    order = (
        db.query(Order)
        .filter(Order.id == payload.order_id)
        .first()
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    if payload.event == "payment_success":
        order.status = "PAID"

        db.commit()
        db.refresh(order)

    return {
        "message": "Webhook processed",
        "order_id": order.id,
        "status": order.status
    }