from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.modules.users.schemas import (
    UserCreate,
    UserResponse
)

from app.modules.users.service import (
    get_all_users,
    get_user_by_id,
    create_user,
    delete_user
)

router = APIRouter()


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = get_user_by_id(user_id, db)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.post("/", response_model=UserResponse)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(
        user.username,
        user.email,
        user.password,
        db
    )


@router.delete("/{user_id}")
def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = get_user_by_id(user_id, db)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    delete_user(user, db)

    return {
        "message": "User deleted successfully"
    }