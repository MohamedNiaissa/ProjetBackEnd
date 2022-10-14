from typing_extensions import Self
from pydantic import BaseModel, Field

from mongo.schemas.comments import CommentCreate, CommentToUpdate


class Comment(BaseModel):
	message: str
	userId: str
	postId: str
	
	@classmethod
	def assert_model(self, user_id: str, comment_data: CommentCreate) -> Self:
		return self(
			userId=user_id,
			message=comment_data.message,
			postId=comment_data.post_id,
		)

	class Config:
		schema_extra = {
			"example": {
				"id": 758,
				"message": "Nice Post you got there",
				"id_user": 30,
				"id_post": 304,
				"nb_like": 0
			}
		}


class CommentUpdate(BaseModel):
	id: str
	message: str
	
	@classmethod
	def assert_model_id(self, id: str, comment_data: CommentToUpdate) -> Self:
		return self(
			id=id,
			message=comment_data.message,
		)

	class Config:
		schema_extra = {
			"example": {
				"id": 758,
				"message": "Nice Post you got there",
				"id_user": 30,
				"id_post": 304,
				"nb_like": 0
			}
		}