import random, string
from typing import Any, Dict
from mongo.schemas.users import UserInDB
from mongo.models.users import User


def random_lower_string() -> str:
    """
    Generate a random character

    Returns:
        str: a string with 32 characters
    """
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_email() -> str:
    """
    Generate a radom email adress baed 

    Returns:
        str: an email adress
    """
    return f"{random_lower_string()}@{random_lower_string()}.com"

def assert_model(user_mongo: Dict) -> User:
    """
    Give the model of the user
    Args:
        user_mongo (Dict): infos of the User

    Returns:
        User: the model of user based on the dictionnary
    """
    user = User.assert_model_id(user_mongo)
    return user