from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.modules.auth.schemas import (
    RegisterRequest,
    LoginRequest,
    TokenResponse
)

from app.modules.auth.service import (
    register_user,
    login_user
)

router = APIRouter()


@router.post("/register")
def register(
    user: RegisterRequest,
    db: Session = Depends(get_db)
):
    created_user = register_user(
        user.username,
        user.email,
        user.password,
        db
    )

    if not created_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "User registered successfully"
    }


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):
    token = login_user(
        user.email,
        user.password,
        db
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }