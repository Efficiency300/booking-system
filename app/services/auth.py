from jose import jwt
from datetime import datetime, timedelta, timezone
from app.core import settings
from passlib.context import CryptContext
from pydantic import EmailStr
from app.core.exceptions import UserIsNotPresentException, IncorrectEmailOrPasswordException
from app.db.dao.users_dao import UsersDao

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt

async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDao.find_by_name(email=email)
    if not user and verify_password(password , user.password):
        raise IncorrectEmailOrPasswordException
    return user