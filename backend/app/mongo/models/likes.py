from pydantic import BaseModel, Field


class LikeBase(BaseModel):
    id: str = Field(alias="_id")
    id_user: str = Field(alias="userId")
    is_liked: bool
    post_id: str = Field(alias="postId")
    comment_id: str = Field(alias="commentId")

    class Config:
        schema_extra = {
            "example": {
                "id": 35,
                "user_id": 234,
                "isLiked": True,
                "post_id": 2345,
                "comment_id": 983,
            }
        }
