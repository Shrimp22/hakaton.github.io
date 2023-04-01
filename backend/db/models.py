from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship

from .database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(30),  primary_key=False, nullable=False)
    last_name = Column(String(30), primary_key=False, nullable=False)
    email = Column(String(30), primary_key=False, unique=True, nullable=False)
    password = Column(String(30), primary_key=False, nullable=False)
    phone = Column(String(20), primary_key=False, nullable=False)
    planer = relationship("Planer", back_populates="user")


class Planer(Base):
    __tablename__ ="planer"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey(Users.id))
    user = relationship("Users", back_populates="planer")