from sqlalchemy.orm import Session

from app.db.models import User


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(user_id: int, db: Session):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def create_user(
    username: str,
    email: str,
    password: str,
    db: Session
):
    user = User(
        username=username,
        email=email,
        password=password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def delete_user(user, db: Session):
    db.delete(user)
    db.commit()