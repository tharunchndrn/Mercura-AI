from sqlalchemy.orm import Session
from app.db.models import Product


def get_all_products(db: Session):
    return db.query(Product).all()


def get_product_by_id(
    product_id: int,
    db: Session
):
    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )


def create_product(
    name: str,
    price: float,
    stock: int,
    db: Session
):
    product = Product(
        name=name,
        price=price,
        stock=stock
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def update_product(
    product: Product,
    name: str,
    price: float,
    stock: int,
    db: Session
):
    product.name = name
    product.price = price
    product.stock = stock

    db.commit()
    db.refresh(product)

    return product


def delete_product(
    product: Product,
    db: Session
):
    db.delete(product)
    db.commit()