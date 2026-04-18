from pydantic import BaseModel
from typing import Optional

class ProfileCreate(BaseModel):
    name: str
    age: Optional[int]


class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None


class ProfileResponse(BaseModel):
    id: int
    name: str
    age: Optional[int]

    class Config:
        from_attributes = True