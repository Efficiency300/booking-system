from fastapi import Request, Depends
from jose import jwt, JWTError ,ExpiredSignatureError


from app.core.exceptions import TokenAbsentException , UserIsNotPresentException , IncorrectTokenFormatException , TokenExpiredException
from app.core.config import settings

from app.db.dao.users_dao import UsersDao


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException

    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:

        raise TokenExpiredException
    except JWTError:
        raise IncorrectTokenFormatException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UsersDao.find_by_id(int(user_id))
    if not user:
        raise UserIsNotPresentException

    return user