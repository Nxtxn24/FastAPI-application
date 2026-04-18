from sqlalchemy import Column, Integer, String, ForeignKey
from db.database import Base
from pydantic import BaseModel
from typing import Optional

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    age = Column(Integer, nullable=True)

