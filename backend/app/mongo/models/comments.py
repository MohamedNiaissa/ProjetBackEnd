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
                "id": "id of comment",
                "message": "comment content",
                "id_user": "id of the comment author",
                "id_post": "id of parent post",
                "nb_like": "current total of likes"
            }
        }
