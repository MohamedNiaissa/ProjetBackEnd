import random, string
from mongo.schemas.users import UserInDB
from mongo.models.users import User


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string()}.com"

def assert_model(user_mongo: UserInDB) -> User:
	user = User(
		password=user_mongo["password"],
		username=user_mongo["username"],
		email=user_mongo["email"],
	)
	user.id = user_mongo["_id"]
	return user