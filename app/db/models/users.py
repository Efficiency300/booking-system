from sqlalchemy import Column, INTEGER, String
from app.db import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)