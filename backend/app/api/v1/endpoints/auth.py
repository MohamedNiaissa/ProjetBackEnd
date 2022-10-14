from typing import Any, List
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard
from crud.crud_users import users
from mongo.schemas.users import UserCreate
from mongo.models.users import User, UserToCreate
from mongo.schemas.token import Token

from core.config import settings

from core.security import (
	create_access_token,
	verify_password,
)

router = APIRouter()


@router.post('/signup')
async def login(signup_data: UserCreate = Body(...)):
	""" Authentification route used for Signup

	Args:
		signup_data (UserCreate, optional): arguments necessary to create a user. Defaults to Body(...).

	Raises:
		HTTPException: raise code 400, user already exist

	Returns:
		Token: jwt token
	"""
	exist = users.exist(signup_data.email)
	if exist:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Username or email is already used"
		)
	
	new_user = UserToCreate.assert_model(signup_data)
	user_id = users.create(new_user)

	return {
		"access_token": create_access_token(
			user_id,
			expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
		),
		"token_type": "bearer",
	}


@router.post('/login')
def login(login_data: UserCreate = Body(...)):
	""" Authentification route used for Login

	Args:
		login_data (UserCreate, optional): arguments necessary to verify a user. Defaults to Body(...).

	Raises:
		HTTPException: raise code 400, user doesn't exist
		HTTPException: raise code 400, email or password is incorrect

	Returns:
		Token: jwt token
	"""
	user_mongo = users.exist(login_data.email)
	if not user_mongo:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Email or password is incorrect"
		)

	user = User.assert_model_id(user_mongo)
	if verify_password(login_data.password, user.password) is False:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Email or password is incorrect"
		)

	access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
	return {
		"access_token": create_access_token(
			user.id, expires_delta=access_token_expires
		),
		"token_type": "bearer",
	}


@router.post("/test-token")
@auth_guard("user")
def test_token(request: Request) -> Any:
	""" Route used for testing

	Args:
		request (Request): request of the endpoint, user details is attached to it

	Returns:
		Any: user documents
	"""
	return request.attach_user