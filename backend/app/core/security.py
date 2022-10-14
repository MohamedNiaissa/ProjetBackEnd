from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext

from core.config import settings
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(
	data: Union[str, Any], expires_delta: timedelta = None
) -> str:
	""" Create a jwt token

	Args:
		data (Union[str, Any]): user id
		expires_delta (timedelta, optional): expiration time for the jwt token. Defaults to None.

	Returns:
		str: encoded jwt token
	"""
	if expires_delta:
		expire = datetime.utcnow() + expires_delta
	else:
		expire = datetime.utcnow() + timedelta(
			minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
		)

	data_to_encode = { "exp": expire, "sub": str(data) }
	encoded_jwt = jwt.encode(
		data_to_encode,
		settings.SECRET_JWT_KEY, 
		algorithm=settings.ENCODE_ALGORITHM
	)

	return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
	""" Verify if the login password match the password in the user document

	Args:
		plain_password (str): request password
		hashed_password (str): passlib hashed password

	Returns:
		bool: check if password match
	"""
	return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
	""" Generate password hash from passlib

	Args:
		password (str): request password

	Returns:
		str: hashed password
	"""
	return pwd_context.hash(password)
