from pydantic import BaseModel, Field


# shared properties of all Reports
class ReportBase(BaseModel):
    reason: int
    user_id: str = Field(alias="userId")
    post_id: str | None = Field(alias="postId")
    comment_id: str | None = Field(alias="commentId")


# properties received by API on creation
class ReportCreate(BaseModel):
    pass


# properties received on update
class ReportUpdate(BaseModel):
    pass


class ReportInDBBase(BaseModel):
    id: str = Field(alias="_id")


# additional properties to return via API
class Report(ReportInDBBase):
    pass


# additional properties stored in data
class ReportInDB(ReportInDBBase):
    pass
