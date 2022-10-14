from pydantic import BaseModel, Field
from typing_extensions import Self
from mongo.schemas.likes import LikeUpdateComment, LikeUpdatePost


class LikeModel:
    id: str
    user_id: str
    is_liked: bool
    comment_id: str
    post_id: str


class LikeBase(BaseModel):
    id: str = Field(alias="_id")
    id_user: str = Field(alias="userId")
    is_liked: bool

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


class LikeComment(LikeBase):
    comment_id: str = Field(alias="commentId")


class LikePost(LikeBase):
    post_id: str = Field(alias="postId")


class LikeToCreatePost(BaseModel):
    userId: str
    isLiked: bool
    postId: str

    @classmethod
    def assert_model(self, user_id: str, like_data: LikeUpdatePost) -> Self:
        return self(
            userId=user_id,
            isLiked=like_data.is_liked,
            postId=like_data.post_id,
        )


class LikeToCreateComment(BaseModel):
    userId: str
    isLiked: bool
    commentId: str

    @classmethod
    def assert_model(self, user_id, like_data: LikeUpdateComment) -> Self:
        print(like_data)
        return self(
            userId=user_id,
            isLiked=like_data.is_liked,
            commentId=like_data.comment_id,
        )
