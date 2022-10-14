from typing import Any, List

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard
from crud.crud_users import users
from mongo.models.users import User
from mongo.schemas.users import UserUpdateProfile

router = APIRouter()


@router.get("/")
@auth_guard("admin")
def get_users(request: Request):
	"""_summary_

	Args:
		request (Request): _description_

	Raises:
		HTTPException: _description_

	Returns:
		_type_: _description_
	"""
	users_list = users.get_all()
	if len(users_list) is 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="No users were found",
		)
	return users_list


@router.get("/me")
@auth_guard("user")
def get_my_user(request: Request):
	"""_summary_

	Args:
		request (Request): _description_

	Returns:
		_type_: _description_
	"""
	return request.attach_user


@router.get("/{id}")
@auth_guard("user")
def get_user_by_id(request: Request, id: str):
	"""_summary_

	Args:
		request (Request): _description_
		id (str): _description_

	Raises:
		HTTPException: _description_

	Returns:
		_type_: _description_
	"""
	user = users.get(id)
	if not user:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="User not found"
		)
	
	user.id = str(user.id)
	return user.__dict__


@router.patch("/me")
@auth_guard("user")
def update_user(request: Request, update_data: UserUpdateProfile = Body(...)):
	"""_summary_

	Args:
		request (Request): _description_
		update_data (UserUpdateProfile, optional): _description_. Defaults to Body(...).

	Returns:
		_type_: _description_
	"""
	user = User.assert_model_id(request.attach_user)
	users.update(user, update_data)
	return { "status": "OK" }


@router.delete("/me")
@auth_guard("user")
def delete_user(request: Request):
	"""_summary_

	Args:
		request (Request): _description_

	Returns:
		_type_: _description_
	"""
	user = User.assert_model_id(request.attach_user)
	users.soft_delete(user)
	return { "status": "OK" }
