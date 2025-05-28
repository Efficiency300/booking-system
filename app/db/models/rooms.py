from sqlalchemy import Column, INTEGER, JSON, String, ForeignKey

from app.db import Base


class Rooms(Base):
    __tablename__ = "rooms"
    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    hotel_id = Column(INTEGER, ForeignKey('hotels.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(INTEGER, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(INTEGER, nullable=False)
    image_id = Column(INTEGER)