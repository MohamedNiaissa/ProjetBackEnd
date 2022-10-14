from fastapi import HTTPException, status
from pymongo.collection import Collection
from pymongo.database import Database
from mongo.schemas.comments import Comment, CommentCreate

from mongo.init_db import get_db
from bson import ObjectId

class CRUDComments():
	db_comments: Collection

	def __init__(self, db: Database):
		self.db_comments = db.get_collection("comments")

	def get_all(self):
		"""_summary_

		Returns:
			_type_: _description_
		"""
		return list(self.db_comments.find())

	def create(self, comment_data: Comment) -> str:
		"""_summary_

		Args:
			comment_data (Comment): _description_

		Returns:
			str: _description_
		"""

		comment_data.userId = ObjectId(comment_data.userId)
		comment_data.postId = ObjectId(comment_data.postId)
		res = self.db_comments.insert_one(comment_data.__dict__)
		return str(res.inserted_id)

	def update(self, comment: Comment):
		"""_summary_

		Args:
			comment (Comment): _description_
		"""
		update_filter = { "_id": ObjectId(comment.id) }
		new_values = {
			"$set": { "message": comment.message }
		}

		self.db_comments.update_one(update_filter, new_values)

	def delete(self, id: str):
		"""_summary_

		Args:
			id (str): _description_

		Raises:
			HTTPException: _description_
		"""
		count = self.db_comments.delete_one({"_id": ObjectId(id)})
		if count.deleted_count is 0:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				details="Comment doesn't exist"
			)


comments = CRUDComments(next(get_db()))