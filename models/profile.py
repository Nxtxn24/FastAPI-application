from sqlalchemy import Column, Integer, String, ForeignKey
from db.database import Base

class ProfileCreate(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    age = Column(Integer, nullable=True)



class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None