from typing import Any, List
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Request, status, Body
from api.deps import auth_guard
from crud.crud_users import users
from mongo.schemas.users import UserCreate
from mongo.models.users import User

from core.config import settings

from utils import (
 	assert_model
)

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
	
	user = users.create(UserCreate(
		email=signup_data.email,
		username=signup_data.username,
		password=signup_data.password
	))

	return {
		"access_token": create_access_token(
			user.id,
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

	user = assert_model(user_mongo)
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
    """
    Test access token
    """
    return request.attach_user