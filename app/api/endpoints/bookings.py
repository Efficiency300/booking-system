from typing import List
from fastapi import APIRouter, Request, Depends
from app.db import BookingsDao
from app.schemas import SBooking
from app.api.dependencies import get_current_user
from app.db import Users
router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)

@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):

    print(user)


