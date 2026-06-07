from pydantic import BaseModel


class PaymentWebhook(BaseModel):
    event: str
    order_id: int