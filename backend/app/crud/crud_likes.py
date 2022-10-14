from turtle import st
from typing import List
from fastapi import HTTPException, status
from pymongo.collection import Collection
from pymongo.database import Database
from mongo.models.likes import LikeToCreatePost, LikeToCreateComment

from mongo.init_db import get_db
from mongo.models.likes import LikeComment, LikePost
from bson import ObjectId

class CRUDLikes():
	db_likes: Collection

	def __init__(self, db: Database):
		self.db_likes = db.get_collection("likes")

	def exist_comment(self, user_id: str, comment_id: str):
		res = self.db_likes.find_one({
			"userId": ObjectId(user_id),
			"commentId": ObjectId(comment_id)
		})
		if res is not None:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="User already liked this comment"
			)

	def exist_post(self, user_id: str, post_id: str):
		res = self.db_likes.find_one({
			"userId": ObjectId(user_id),
			"postId": ObjectId(post_id)
		})
		if res is not None:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="User already liked this post"
			)

	def get_by_post_id(self, id: str) -> List[LikePost]:
		"""
		This function fetch the likes linked to the post chosen by its ID from the collection called likes

		Args:
			id (int): id of the like 

		Returns:
			JSON: infos of that like 
		"""
		return list(self.db_likes.find({"postId": ObjectId(id)}))

	def get_by_comment_id(self, id: str) -> List[LikeComment]:
		"""
		This function fetch the likes linked to the comment chosen by its ID from the collection called likes

		Args:
			id (int): id of the likes

		Returns:
			JSON: infos of that like 
		"""
		return list(self.db_likes.find({"commentId": ObjectId(id)}))

	def create_on_post(self, likes_data: LikeToCreatePost) -> str:
		"""_summary_

		Args:
			likes_data (LikeToCreatePost): _description_

		Returns:
			_type_: _description_
		"""
		self.exist_post(likes_data.userId, likes_data.postId)
		likes_data.postId = ObjectId(likes_data.postId)
		likes_data.userId = ObjectId(likes_data.userId)
		res = self.db_likes.insert_one(likes_data.__dict__)
		return str(res.inserted_id)

	def create_on_comment(self, likes_data: LikeToCreateComment) -> str:
		"""_summary_

		Args:
			likes_data (LikeToCreatePost): _description_

		Returns:
			_type_: _description_
		"""
		self.exist_comment(likes_data.userId, likes_data.commentId)
		likes_data.commentId = ObjectId(likes_data.commentId)
		likes_data.userId = ObjectId(likes_data.userId)
		res = self.db_likes.insert_one(likes_data.__dict__)
		return str(res.inserted_id)

	def delete(self, id: str) -> None:
		"""_summary_

		Args:
			id (str): _description_

		Raises:
			HTTPException: _description_
		"""
		count = self.db_likes.delete_one({"_id": ObjectId(id)})
		if count.deleted_count == 0:
			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="Like doesn't exist"
			)


likes = CRUDLikes(next(get_db()))