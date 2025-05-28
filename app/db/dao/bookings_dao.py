from app.db import Bookings
from app.db import BaseDao

class BookingsDao(BaseDao):
    model=Bookings
