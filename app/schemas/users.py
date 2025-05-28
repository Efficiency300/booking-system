from pydantic import BaseModel, EmailStr


class SUser(BaseModel):
    email: EmailStr
    hashed_password: str
