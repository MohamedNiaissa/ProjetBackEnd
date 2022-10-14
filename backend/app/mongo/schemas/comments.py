from pydantic import BaseModel, Field


# shared properties of all comments
class CommentBase(BaseModel):
    message: str


# properties received on comment creation
class CommentCreate(CommentBase):
    # user_id: str = Field(alias="userId")
    post_id: str


# properties received via API on update
class CommentToUpdate(CommentBase):
    pass


class CommentInDBBase(CommentBase):
    id: str = Field(alias="_id")


class Comment(CommentInDBBase):
    pass


class UserInDB(CommentInDBBase):
    pass
