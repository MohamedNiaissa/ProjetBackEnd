from pydantic import BaseModel, Field


# shared properties of likes
class LikeBase(BaseModel):
    isLiked: bool


# properties to receive on like creation
class LikeCreate(LikeBase):
    pass


# properties to receive via API on update
class LikeUpdate(LikeBase):
    pass


class LikeInDBBase(LikeBase):
    user_id: str = Field(alias="_id")
    post_id: str = Field(alias="postId")


# additional properties stored in db
class LikeInDB(LikeInDBBase):
    comment_id: str | None = Field(alias="commentId")
