from fastapi import APIRouter , Response
from app.schemas.auth import SUserAuth
from app.core.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException
from app.services.auth import get_password_hash, authenticate_user, create_access_token
from app.db import UsersDao

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post("/register")
async def get_current_user(user_data: SUserAuth):
    exisiting_user = await UsersDao.find_by_name(email=user_data.email)
    if exisiting_user:
        raise UserAlreadyExistsException
    hashed_password = await get_password_hash(password=user_data.password)
    await UsersDao.add(email=user_data.email, hashed_password=hashed_password)

@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}

@router.post("/logout")
async def logout_user(response: Response):
        response.delete_cookie("booking_access_token")
        return {"message": "Successfully logged out"}