from sqlalchemy import Column, INTEGER, ForeignKey, DATE, Computed
from app.db import Base

class Bookings(Base):
    __tablename__ = "bookings"
    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    room_id = Column(INTEGER, ForeignKey("rooms.id"))
    user_id = Column(INTEGER, ForeignKey("users.id"))
    date_from = Column(DATE, nullable=False)
    date_to = Column(DATE, nullable=False)
    price = Column(INTEGER, nullable=False)
    total_cost = Column(INTEGER, Computed("(date_to - date_from) * price"))
    total_days = Column(INTEGER, Computed("(date_to - date_from)"))