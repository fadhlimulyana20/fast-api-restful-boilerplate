from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from models.base import Base
from models.item import Items

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    name = Column(String(150))
    password = Column(String(200))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_active = Column(Boolean, default=True)

    # items = relationship("Items", back_populates="owner")