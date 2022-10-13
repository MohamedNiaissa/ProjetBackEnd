from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    id: str = Field(alias="_id")
    username: str
    email: EmailStr
    password: str
    token: str
    salt: str
    refresh_token: str

    class Config:
        schema_extra = {
            "example": {
                "id": 43 ,
                "username": "GeneralUserName",
                "email": "Generic.mail@gmail.com",
                "password": "password123",
                "token": "Byxm1iW5J5KMzdbSKwn37CgncQ0MeEhv",
                "salt": "superSecretKey",
                "refresh_token": "rMRCZVOfcK"
            }
        }
