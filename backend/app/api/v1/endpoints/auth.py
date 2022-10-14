from typing import Any, List
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard
from crud.crud_users import users
from mongo.schemas.users import UserCreate
from mongo.models.users import User, UserToCreate

from core.config import settings

from core.security import (
	create_access_token,
	verify_password,
)

router = APIRouter()


@router.post('/signup')
async def login(signup_data: UserCreate = Body(...)):
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
	"""_summary_

	Args:
		request (Request): _description_

	Returns:
		Any: _description_
	"""
	return request.attach_user