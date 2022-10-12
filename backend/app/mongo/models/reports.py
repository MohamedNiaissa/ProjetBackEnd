from pydantic import BaseModel, Field


class ReportBase(BaseModel):
    id: str = Field(alias="_id")
    user_id: str = Field(alias="userId")
    post_id: str | None = Field(alias="postId")
    comment_id: str | None = Field(alias="commentId")
    reason: int

    class Config:
        schema_extra = {
            "example": {
                "id": 12,
                "user_id": 930,
                "post_id": 3984,
                "comment_id": 22,
                "reason": 1
            }
        }
