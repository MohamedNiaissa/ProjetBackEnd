from typing import Any, List

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard

from mongo.schemas.likes import *
from mongo.schemas.likes import LikeUpdateComment, LikeUpdatePost
from mongo.models.likes import LikeToCreateComment, LikeToCreatePost
from crud.crud_likes import likes

router = APIRouter()


@router.get("/posts/{id}")
def get_likes_by_post_id(id: str):
	"""_summary_

	Args:
		id (str): _description_

	Raises:
		HTTPException: _description_

	Returns:
		_type_: _description_
	"""
	list_likes = likes.get_by_post_id(id)
	if len(list_likes) is 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Current post does not have any like"
		)
  
	return list_likes


@router.get("/comments/{id}")
def get_likes_by_comment_id(id: str):
	"""_summary_

	Args:
		id (str): _description_

	Raises:
		HTTPException: _description_

	Returns:
		_type_: _description_
	"""
	list_likes = likes.get_by_comment_id(id)
	if len(list_likes) is 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Current comment does not have any like"
		)

	return list_likes


@router.post("/posts", response_model=LikeCreate)
@auth_guard("user")
def manage_like_on_post(request: Request, likes_state: LikeUpdatePost = Body(...)):
	"""_summary_

	Args:
		request (Request): _description_
		likes_state (LikeUpdatePost, optional): _description_. Defaults to Body(...).

	Returns:
		_type_: _description_
	"""
	is_liked = likes_state.is_liked
	if is_liked is True:
		likes_data = LikeToCreatePost.assert_model(request.attach_user["id"], likes_state)
		id = likes.create_on_post(likes_data)
		return { "status": "OK", "post_id": id }
	else:
		likes.delete(likes_state.id)
		return { "status": "0K" }


@router.post("/comments")
@auth_guard("user")
def manage_like_on_comment(request: Request, likes_state: LikeUpdateComment = Body(...)):
	"""_summary_

	Args:
		request (Request): _description_
		likes_state (LikeUpdateComment, optional): _description_. Defaults to Body(...).

	Returns:
		_type_: _description_
	"""
	is_liked = likes_state.is_liked
	if is_liked is True:
		likes_data = LikeToCreateComment.assert_model(request.attach_user["id"], likes_state)
		id = likes.create_on_comment(likes_data)
		return { "status": "OK", "commend_id": id }
	else:
		likes.delete(likes_state.id)
		return { "status": "0K" }
