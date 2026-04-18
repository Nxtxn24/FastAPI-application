from pydantic import BaseModel
from typing import Optional

class ProfileCreate(BaseModel):
    name: str
    age: Optional[int]