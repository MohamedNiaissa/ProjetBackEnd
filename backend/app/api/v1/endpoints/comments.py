from typing import Any, List

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard

from mongo.schemas.comments import *
from crud.crud_comments import comments
from mongo.schemas.comments import CommentCreate, CommentToUpdate
from mongo.models.comments import Comment, CommentUpdate

router = APIRouter()


@router.get("/", response_model=Comment)
def get_comments():
	"""_summary_

	Raises:
		HTTPException: _description_

	Returns:
		_type_: _description_
	"""
	comments_list = comments.get_all()
	if len(comments_list) is 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="No comments were found",
		)
	return comments_list


@router.post("/", response_model=CommentCreate)
@auth_guard("user")
def create_comment(request: Request, comment_create: CommentCreate = Body(...)):
	"""_summary_

	Args:
		request (Request): _description_
		comment_create (CommentCreate, optional): _description_. Defaults to Body(...).

	Returns:
		_type_: _description_
	"""
	comment_data = Comment.assert_model(request.attach_user["id"], comment_create)
	id = comments.create(comment_data)
	return { "status": "OK", "comment_id": id }


@router.patch("/{id}", response_model=CommentUpdate)
@auth_guard("user")
def update_comment(request: Request, id: str, comment_update: CommentToUpdate = Body(...)):
	"""_summary_

	Args:
		request (Request): _description_
		id (str): _description_
		comment_update (CommentToUpdate, optional): _description_. Defaults to Body(...).

	Returns:
		_type_: _description_
	"""
	comment = CommentUpdate.assert_model_id(id, comment_update)
	comments.update(comment)
	return { "status": "OK" }


@router.delete("/{id}")
@auth_guard("user")
def delete_comment(request: Request, id: str):
	"""_summary_

	Args:
		request (Request): _description_

	Returns:
		_type_: _description_
	"""
	comments.delete(id)
	return { "status": "OK" }