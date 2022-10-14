from typing import Any, List
from urllib import response

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard

from mongo.schemas.likes import *
from mongo.schemas.likes import LikeUpdateComment, LikeUpdatePost
from mongo.models.likes import LikeToCreateComment, LikeToCreatePost
from crud.crud_likes import likes
from mongo.schemas.token import StatusOK

router = APIRouter()


@router.get("/posts/{id}", response_model=List[LikeUpdatePost])
def get_likes_by_post_id(id: str):
	"""Gets like status from a specified post

	Args:
		id (str): id of the post to get status from

	Raises:
		HTTPException: raise 404 if no likes were found or if no posts were found

	Returns:
		List : List of information of that like
	"""

	list_likes = likes.get_by_post_id(id)
	if len(list_likes) is 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Current post does not have any like"
		)
  
	return list_likes


@router.get("/comments/{id}", response_model=List[LikeUpdateComment])
def get_likes_by_comment_id(id: str):
	"""Gets like status from a specified comment

	Args:
		id(str): id of the comment to get status from

	Raises:
		HTTPException: raise 404 if no likes were found or if no comments were found

	Returns:
		List: list of infos of that like
"""

	list_likes = likes.get_by_comment_id(id)
	if len(list_likes) is 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="Current comment does not have any like"
		)

	return list_likes


@router.post("/posts", response_model=StatusOK)
@auth_guard("user")
def manage_like_on_post(request: Request, likes_state: LikeUpdatePost = Body(...)):
	"""Changes the status of the like and infos linked to the comment such as the commentID and userID

	Args:
		request (Request):  request of the endpoint, post details are attached to it.

	Raises:
		HTTPException: raise 404 if no comment is found

	Returns:
		Status: Ok
		post_id: id of the liked post if it was already liked
"""
	is_liked = likes_state.is_liked
	if is_liked is True:
		likes_data = LikeToCreatePost.assert_model(request.attach_user["id"], likes_state)
		id = likes.create_on_post(likes_data)
		return { "status": "OK", "post_id": id }
	else:
		likes.delete(likes_state.id)
		return { "status": "0K" }


@router.post("/comments", response_model=StatusOK)
@auth_guard("user")
def manage_like_on_comment(request: Request, likes_state: LikeUpdateComment = Body(...)):
	"""Changes the status of the like and infos linked to the comment such as the commentID and userID

	Args:
		request (Request): request of the endpoint, comment details are attached to it.

	Raises:
		HTTPException: raise 404 if no comment is found

	Returns:
		Status: Ok
		post_id: id of the liked comment if it was already liked
"""
	is_liked = likes_state.is_liked
	if is_liked is True:
		likes_data = LikeToCreateComment.assert_model(request.attach_user["id"], likes_state)
		id = likes.create_on_comment(likes_data)
		return { "status": "OK", "commend_id": id }
	else:
		likes.delete(likes_state.id)
		return { "status": "0K" }
