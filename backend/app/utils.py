import random, string
from typing import Any, Dict
from mongo.schemas.users import UserInDB
from mongo.models.users import User


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"

def assert_model(user_mongo: Dict) -> User:
	user = User.assert_model_id(user_mongo)
	return user