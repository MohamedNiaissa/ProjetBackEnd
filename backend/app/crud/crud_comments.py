from typing import List
from fastapi import HTTPException, status
from pymongo.collection import Collection
from pymongo.database import Database
from mongo.schemas.comments import Comment, CommentCreate

from mongo.init_db import get_db
from bson import ObjectId

class CRUDComments():
	db_comments: Collection

	def __init__(self, db: Database):
		""" Init Comments class with the required database collection

		Args:
			db (Database): mongodb database
		"""
		self.db_comments = db.get_collection("comments")

	def get_all(self) -> List:
		""" Get all documents in the collection comments

		Returns:
			List: comments documents
		"""
		return list(self.db_comments.find())

	def create(self, comment_data: Comment) -> str:
		""" Create a comment in the database

		Args:
			comment_data (Comment): comment data

		Returns:
			str: id of the comment
		"""

		comment_data.userId = ObjectId(comment_data.userId)
		comment_data.postId = ObjectId(comment_data.postId)
		res = self.db_comments.insert_one(comment_data.__dict__)
		return str(res.inserted_id)

	def update(self, comment: Comment):
		""" Update a comment in the database

		Args:
			comment (Comment): comment data
		"""
		update_filter = { "_id": ObjectId(comment.id) }
		new_values = {
			"$set": { "message": comment.message }
		}

		self.db_comments.update_one(update_filter, new_values)

	def delete(self, id: str):
		""" Delete a comment in the database

		Args:
			id (str): id of the comment

		Raises:
			HTTPException: raise 400 if comment was not found
		"""
		count = self.db_comments.delete_one({"_id": ObjectId(id)})
		if count.deleted_count == 0:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="Comment doesn't exist"
			)


comments = CRUDComments(next(get_db()))