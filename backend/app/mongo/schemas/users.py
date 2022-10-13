from typing import Optional
from pydantic import BaseModel, EmailStr, Field


# Shared properties of user
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    isAdmin: bool = False


# properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# properties to receive via API on update
class UserUpdate(UserBase):
    password: str | None = Field(alias="_id")


class UserInDBBase(UserBase):
	id: Optional[str] = Field(alias="_id")


# additional properties to return via API
class User(UserInDBBase):
    pass


# additional properties to store in DB
class UserInDB(UserInDBBase):
    password: str
