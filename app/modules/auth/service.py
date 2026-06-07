from sqlalchemy.orm import Session

from app.db.models import User

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(
    username: str,
    email: str,
    password: str,
    db: Session
):
    existing_user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if existing_user:
        return None

    user = User(
        username=username,
        email=email,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def authenticate_user(
    email: str,
    password: str,
    db: Session
):
    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    return user


def login_user(
    email: str,
    password: str,
    db: Session
):
    user = authenticate_user(
        email,
        password,
        db
    )

    if not user:
        return None

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return token