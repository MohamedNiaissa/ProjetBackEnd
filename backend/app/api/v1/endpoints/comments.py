from typing import Any, List

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard

from mongo.schemas.comments import *
from crud.crud_comments import comments
from mongo.schemas.comments import CommentCreate, CommentToUpdate
from mongo.models.comments import Comment, CommentUpdate

router = APIRouter()


@router.get("/post/{id}", response_model=Comment)
def get_comments(id: str) -> List:
	""" Get all the reports from the database

	Raises:
		HTTPException: raise 404 if no comments were found

	Returns:
		List: comments documents
	"""
	comments_list = comments.get_all(id)
	if len(comments_list) is 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="No comments were found",
		)
	return comments_list


@router.post("/", response_model=CommentCreate)
@auth_guard("user")
def create_comment(request: Request, comment_create: CommentCreate = Body(...)) -> Any:
	""" User can create a comment

	Args:
		request (Request): request of the endpoint, user details are attached to it
		comment_create (CommentCreate, optional): arguments necessary to create a comment . Defaults to Body(...).

	Returns:
		Any : default status for code 200, commentId attached to it
	"""
	comment_data = Comment.assert_model(request.attach_user["id"], comment_create)
	id = comments.create(comment_data)
	return { "status": "OK", "comment_id": id }


@router.patch("/{id}", response_model=CommentUpdate)
@auth_guard("user")
def update_comment(request: Request, id: str, comment_update: CommentToUpdate = Body(...)) -> Any:
	""" Update a comment content in the database

	Args:
		request (Request): request of the endpoint, user details are attached to it
		id (str): id of the comment
		comment_update (CommentToUpdate, optional): arguments necessary to update a comment . Defaults to Body(...).

	Returns:
		Any: default status for code 200
	"""
	comment = CommentUpdate.assert_model_id(id, comment_update)
	comments.update(comment)
	return { "status": "OK" }


@router.delete("/{id}")
@auth_guard("user")
def delete_comment(request: Request, id: str):
	""" Delete a comment in the database

	Args:
		request (Request): request of the endpoint, user details are attached to it

	Returns:
		Any: default status for code 200
	"""
	comments.delete(id)
	return { "status": "OK" }