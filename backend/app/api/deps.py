from typing import Any
from pymongo.database import Database

from functools import wraps
from fastapi import Request

from fastapi import HTTPException, status

from pydantic import ValidationError
from jose import jwt, JWTError

from core.config import settings

from mongo.models.users import User
from crud.crud_users import users


def auth_guard(role: str):
	""" Wrapper decorator used to pass the user role
		Auth Guard is a decorator used for verifying the jwt token
		It also attach the user to the Request

	Args:
		role (str): user role
	"""
	def decorator_auth_guard(handler):
		""" Function that will define the auth_guard decorator

		Args:
			handler (_type_): Self

		Raises:
			HTTPException: raise 403 if the Bearer is not present
			HTTPException: raise 403 if the requested user is not admin when accesing admin routes

		Returns:
			Self: handler
		"""
		@wraps(handler)
		async def wrapper(request: Request, *args, **kwargs):
			auth: str = request.headers.get("authorization")
			if auth is None or "Bearer" not in auth:
				raise HTTPException(
					status_code=status.HTTP_403_FORBIDDEN,
					detail="You are not authorized to access this resource"
				)
			
			token = auth.replace("Bearer ", "")
			user = await get_user_from_jwt(token)
			if role is "admin" and user.isAdmin is False:
				raise HTTPException(
					status_code=status.HTTP_403_FORBIDDEN,
					detail="You are not authorized to access this resource"
				)

			user.id = str(user.id)
			request.attach_user = user.__dict__
			return handler(request, *args, **kwargs)

		return wrapper
	return decorator_auth_guard


async def get_user_from_jwt(token = str) -> User:
	""" Verify the jwt token and decode the user details

	Args:
		token (_type_, optional): jwt token. Defaults to str.

	Raises:
		HTTPException: raise 403 if the token failed to be decoded
		HTTPException: raise 404 if the user was not found
		HTTPException: raise 404 if the user email was not found

	Returns:
		User: user document
	"""
	try:
		payload = jwt.decode(
			token, settings.SECRET_JWT_KEY, algorithms=[settings.ENCODE_ALGORITHM]
		)
		token_data = payload.get("sub")
	except (JWTError, ValidationError):
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail="Credentials weren't validated",
		)

	user = users.get(token_data)
	if not user:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="User not found"
		)
	elif user.email is None:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="User not found"
		)

	return user