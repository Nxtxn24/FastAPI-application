from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.profile import Profile
from models.user import User
from schemas.profile import ProfileCreate, ProfileResponse



def get_profile(db: Session, user: User):
    profile = db.query(Profile).filter(Profile.user_id == user.id).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return profile



def create_profile(db: Session, user: User, profile_data):
    new_profile = Profile(
        user_id=user.id,
        name=profile_data.name,
        age=profile_data.age
    )

    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)

    return new_profile



def update_profile(db: Session, profile: ProfileCreate, update_data: dict):
    for key, value in update_data.items():
        setattr(profile, key, value)

    db.commit()
    db.refresh(profile)

    return profile