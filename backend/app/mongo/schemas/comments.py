from pydantic import BaseModel, Field


# shared properties of all comments
class CommentBase(BaseModel):
    id_user: str = Field(alias="userId")
    message: str
    nb_like: int


# properties received on comment creation
class CommentCreate(CommentBase):
    id_post: str = Field(alias="postId")


# properties received via API on update
class CommentUpdate(CommentBase):
    pass


class CommentInDBBase(CommentBase):
    id: str = Field(alias="_id")


class Comment(CommentInDBBase):
    pass


class UserInDB(CommentInDBBase):
    pass
