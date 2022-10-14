from typing import Dict, Optional
from typing_extensions import Self
from pydantic import BaseModel, EmailStr, Field as PydanticField
from bson import ObjectId
from mongo.schemas.users import UserCreate

from core.security import (
	get_password_hash
)

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class User(BaseModel):
    id: Optional[PyObjectId]
    username: Optional[str] = ...
    profile_picture: Optional[str] = None
    email: EmailStr
    password: str
    isAdmin: bool = False
    
    @classmethod
    def assert_model_id(self, user_data: Dict) -> Self:
        if "_id" in user_data:
            id = str(user_data["_id"])
        else:
            id = str(user_data["id"])
        
        return self(
            id=id,
            username=user_data["username"],
            email=user_data["email"],
            password=user_data["password"],
            isAdmin=user_data["isAdmin"],
            profile_picture=user_data["profile_picture"]
        )

    class Config:
        schema_extra = {
            "example": {
                "id": 43,
                "username": "GeneralUserName",
                "email": "Generic.mail@gmail.com",
                "password": "password123",
                "token": "Byxm1iW5J5KMzdbSKwn37CgncQ0MeEhv",
                "salt": "superSecretKey",
                "refresh_token": "rMRCZVOfcK"
            }
        }


class UserToCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    isAdmin: bool = False
    profile_picture: str = None
    
    @classmethod
    def assert_model(self, user_data: UserCreate) -> Self:
        return self(
            username=user_data.username,
            email=user_data.email,
            password=get_password_hash(user_data.password),
        )