from typing import Optional
from pydantic import BaseModel, Field


# shared properties of likes
class LikeBase(BaseModel):
    id: Optional[str] = Field(default=None)
    is_liked: bool


# properties to receive on like creation
class LikeUpdatePost(LikeBase):
    post_id: str


# properties to receive via API on update
class LikeUpdateComment(LikeBase):
    comment_id: str


# class LikeInDBBase(LikeBase):
#     user_id: str = Field(alias="_id")
#     post_id: str = Field(alias="postId")


# # additional properties stored in db
# class LikeInDB(LikeInDBBase):
#     comment_id: str | None = Field(alias="commentId")
