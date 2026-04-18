from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    age: Optional[int]

    class Config:
        from_attributes = True