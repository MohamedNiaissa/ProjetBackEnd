from pydantic import BaseModel, Field


class CommentBase(BaseModel):
    id: str = Field(alias="_id")
    message: str
    id_user: str = Field(alias="userId")
    id_post: str = Field(alias="postId")
    nb_like: int

    # might need to tag id_user
    # #and id_post more appropriately
    # #since they are supposed
    # to be ObjectIds

    class Config:
        schema_extra = {
            "example": {
                "id": 758,
                "message": "Nice Post you got there",
                "id_user": 30,
                "id_post": 304,
                "nb_like": 0
            }
        }
