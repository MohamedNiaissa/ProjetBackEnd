from typing import Generator, Any
from webbrowser import get
from pymongo.database import Database

from functools import wraps
from fastapi import Request

from fastapi import Depends, HTTPException, status

from pydantic import ValidationError
from jose import jwt, JWTError

from core.config import settings
from mongo.init_db import client


def get_db() -> Generator:
	db = client[settings.MONGO_DB_NAME]
	yield db


def auth_guard(role: str):
	def decorator_auth_guard(handler):
		@wraps(handler)
		async def wrapper(request: Request, *args, **kwargs):
			auth: str = request.headers.get("authorization")
			if auth is None or "Bearer" not in auth:
				raise HTTPException(
					status_code=status.HTTP_403_FORBIDDEN,
					detail="You are not authorized to access this resource"
				)
			
			token = auth.replace("Bearer ", "")
			user = await get_user_from_jwt(next(get_db()), token)
			if role is "admin" and user["isAdmin"] is False:
				raise HTTPException(
					status_code=status.HTTP_403_FORBIDDEN,
					detail="You are not authorized to access this resource"
				)

			request.attach_user = user
			return handler(request, *args, **kwargs)

		return wrapper
	return decorator_auth_guard


async def get_user_from_jwt(
	db: Database = Depends(get_db),
	token = str,
) -> Any:
	# try:
	# 	payload = jwt.decode(
	# 		token, settings.SECRET_JWT_KEY, algorithms=[settings.ENCODE_ALGORITHM]
	# 	)
	# 	token_data = "" #Schema token
	# except (JWTError, ValidationError):
	# 	raise HTTPException(
	# 		status_code=status.HTTP_403_FORBIDDEN,
	# 		detail="Credentials weren't validated",
	# 	)

	# print(payload)
	user = dict({ "name": "test", "isAdmin": True }) #CRUD get user
	print(user)
	if not user:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="User not found"
		)
	return user