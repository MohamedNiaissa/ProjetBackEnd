from typing import Optional
from pydantic import BaseModel, EmailStr, Field as PydanticField
from bson import ObjectId

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
    id: Optional[PyObjectId] = PydanticField(default_factory=PyObjectId, alias="_id")
    username: str
    email: EmailStr
    password: str
    isAdmin: bool = False

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