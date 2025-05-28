from fastapi import APIRouter


router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"],
)


@router.get("")
async def get_rooms():
    pass
