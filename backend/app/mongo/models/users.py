from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    id: str = Field(alias="_id")
    username: str
    email: EmailStr
    password: str
    token: str
    salt: str
    refresh_token: str
