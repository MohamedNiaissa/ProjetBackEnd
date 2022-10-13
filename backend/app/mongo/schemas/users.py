from pydantic import BaseModel, EmailStr, Field


# Shared properties of user
class UserBase(BaseModel):
    username: str
    mail: EmailStr
    isAdmin: bool | None = None


# properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# properties to receive via API on update
class UserUpdate(UserBase):
    password: str | None = Field(alias="_id")


class UserInDBBase(UserBase):
    id: str = Field(alias="_id")
    salt: str
    token: str
    refresh_token: str


# additional properties to return via API
class User(UserInDBBase):
    pass


# additional properties to store in DB
class UserInDB(UserInDBBase):
    pass
