from pydantic import BaseModel, Field


# properties shared by all posts
class PostBase(BaseModel):
    title: str
    description: str
    nbLike: int | None
    tag: str | None = None


# properties received on post creation
class PostCreate(PostBase):
    pass


# properties to receive on Update
class PostUpdate(PostBase):
    pass


class PostInDBBase(PostBase):
    id: str = Field(alias="_id")
    id_user: str = Field(alias="userId")


# additional properties to receive by API
class Post(PostInDBBase):
    pass


# additional properties stored in db
class PostInDB(PostInDBBase):
    pass
