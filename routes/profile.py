from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from models.user import User
from models.profile import ProfileCreate
from schemas.profile import ProfileCreate
from core.current import get_current_user

router = APIRouter()


@router.post("/set_profile")
def create_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.name == current_user).first()

    new_profile = Profile(
        user_id=user.id,
        name=profile.name,
        age=profile.age
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile


@router.get("/me")
def get_profile(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.name == current_user).first()

    profile = db.query(Profile).filter(Profile.user_id == user.id).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile