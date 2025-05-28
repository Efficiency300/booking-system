from sqlalchemy import Column, INTEGER, JSON, String

from app.db import Base


class Hotels(Base):
    __tablename__ = "hotels"
    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(INTEGER, nullable=False)
    image_id = Column(INTEGER)