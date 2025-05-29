from datetime import date
from typing import List
from fastapi import APIRouter, Depends
from app.db import BookingsDao
from app.schemas import SBooking
from app.api.dependencies import get_current_user
from app.db import Users
router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> List[SBooking]:

    return await BookingsDao.find_all(user_id=user.id)



@router.post("")
async def add_bookings(
        rooms_id: int,
        date_from: date,
        date_to: date,
        user: Users = Depends(get_current_user)):

    return await BookingsDao.add(user.id , rooms_id , date_from , date_to)


