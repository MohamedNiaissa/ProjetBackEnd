from typing import Generator, Any
from pymongo.database import Database

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from pydantic import ValidationError
from jose import jwt, JWTError

from core.config import settings
from mongo.init_db import client


def get_db() -> Generator:
	db = client[settings.MONGO_DB_NAME]
	yield db


def auth_guard(
	db: Database = Depends(get_db), token = str
) -> Any:
	try:
		payload = jwt.decode(
			token, settings.SECRET_JWT_KEY, algorithms=[settings.ENCODE_ALGORITHM]
		)
		token_data = "" #Schema token
	except (JWTError, ValidationError):
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail="Credentials weren't validated",
		)

	user = "" #CRUD get user
	if not user:
		raise HTTPException(
			status_code=status.HTTP_404_NOT_FOUND,
			detail="User not found"
		)
	return user