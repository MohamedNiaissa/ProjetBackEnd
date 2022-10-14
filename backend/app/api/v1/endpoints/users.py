from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard

from mongo.schemas.users import *
from crud.crud_users import users
from mongo.models.users import User
from mongo.schemas.users import UserUpdateProfile
from mongo.schemas.token import StatusOK

from mongo.models.users import User
router = APIRouter()


@router.get("/", response_model=List[User])
@auth_guard("admin")
def get_users(request: Request):
	"""Gets all users from the database

	Args:
		request (Request): request of the endpoint, details of each user is attached to it

	Raises:
		HTTPException: raise 404 if no users where found

	Returns:
		List: All informations from all users
	"""
	users_list = users.get_all()
	if len(users_list) is 0:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="No users were found",
		)
	return users_list


@router.get("/me", response_model=Dict)
@auth_guard("user")
def get_my_user(request: Request):
	"""Gets current logged-in user info from the database

	Args:
		request (Request): request of the endpoint, user details are attached to it

	Returns:
		JSON: All informations from the attached user
	"""
	return request.attach_user


@router.get("/{id}", response_model=User)
def get_user_by_id(request: Request, id: str):
	"""Gets informations of a specified user

	Args:
		request (Request): request of the endpoint, specified user details are attached to it
		id (str): id of the specified user

	Raises:
		HTTPException: raises 404 if no user matches the id

	Returns:
		dict: Dictionary of the correspondant user informations
	"""
	user = users.get(id)
	if not user:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="User not found"
		)
	
	user.id = str(user.id)
	return user.__dict__


@router.patch("/me", response_model=StatusOK)
@auth_guard("user")
def update_user(request: Request, update_data: UserUpdateProfile = Body(...)):
	"""Update current user's informations

	Args:
		request (Request): Request of the endpoint, user's details are attached to it
		update_data (UserUpdateProfile, optional): Data to be updated. Defaults to Body(...).

	Returns:
		status: OK on completion
	"""
	user = User.assert_model_id(request.attach_user)
	users.update(user, update_data)
	return { "status": "OK" }


@router.delete("/me", response_model=StatusOK)
@auth_guard("user")
def delete_user(request: Request):
	"""Deletes current user's informations

	Args:
		request (Request): Request of the endpoint, user's details are attached to it

	Returns:
		status: Ok on completion
	"""
	user = User.assert_model_id(request.attach_user)
	users.soft_delete(user)
	return { "status": "OK" }