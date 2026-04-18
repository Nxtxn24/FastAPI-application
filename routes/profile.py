from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from core.current import get_current_user

from models.user import User
from schemas.profile import ProfileCreate, ProfileUpdate, ProfileResponse

from service.profile_service import (
    get_profile,
    create_profile,
    update_profile
)

router = APIRouter()



@router.post("/set_profile", response_model=ProfileResponse)
def create_profile_route(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.name == current_user).first()

    return create_profile(db, user, profile)


@router.get("/me", response_model=ProfileResponse)
def get_profile_route(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.name == current_user).first()

    return get_profile(db, user)


@router.patch("/me", response_model=ProfileResponse)
def update_profile_route(
    profile_update: ProfileUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.name == current_user).first()

    profile = get_profile(db, user)

    update_data = profile_update.model_dump(exclude_unset=True)

    return update_profile(db, profile, update_data)