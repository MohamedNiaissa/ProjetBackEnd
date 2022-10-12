from pydantic import BaseModel, Field


class PostBase(BaseModel):
    id: str = Field(alias="_id")
    title: str
    message: str
    user_id: str = Field(alias="userId")
    tag: str
    nb_like: int

    class Config:
        schema_extra = {
            "example": {
                "id": 35,
                "title": "cooking for dummies",
                "message": "a nice recipe",
                "user_id": 234,
                "tag": "culinary",
                "nb_like": 23
            }
        }
