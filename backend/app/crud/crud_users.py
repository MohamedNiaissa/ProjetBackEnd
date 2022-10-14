import json
from typing import Any, List
from fastapi import HTTPException, status
from pymongo.collection import Collection
from pymongo.database import Database

from mongo.init_db import get_db
from mongo.schemas.users import UserInDB
from mongo.models.users import User, UserToCreate
from bson import ObjectId

class CRUDUsers():
    db_users: Collection

    def __init__(self, db: Database):
        self.db_users = db.get_collection("users")

    def exist(self, email: str) -> UserInDB | None:
        return self.db_users.find_one({"email": email})

    def get(self, id: str) -> User | None:
        try:
            user = self.db_users.find_one({"_id": ObjectId(id)})
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User not found"
                )
            return User.assert_model_id(user)
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User not found"
            )

    def get_all(self) -> List:
        """
        This function fetch all the users from the collection called users 

        Returns:
            JSON: informations of all users
        """
        return list(self.db_users.find())

    def create(self, user: UserToCreate) -> str:
        """
        Create a user and insert it on the users collection

        Returns:
            JSON: inserted infos for the created user
        """
        res = self.db_users.insert_one(user.__dict__)
        return res.inserted_id

    def update(self, current_user: User, data_update: User):
        """
        Modify one or more specific data from a specific user

        Args:
            id (number): id of the user

        Returns:
            JSON: All the informations of this same user 
        """
        json_field = { **data_update.__dict__ }
        json_field.pop("isAdmin")
        
        if "email" in json_field and json_field["email"] is None:
            json_field.pop("email")
        
        if "username" in json_field and json_field["username"] is None:
            json_field.pop("username")

        if "profile_picture" in json_field and json_field["profile_picture"] is None:
            json_field.pop("profile_picture")
        
        update_filter = { "_id": ObjectId(current_user.id) }
        new_values = {
            "$set": { **json_field }
        }

        self.db_users.update_one(update_filter, new_values)

    def soft_delete(self, current_user: User) -> None:
        """
        Delete a specific user

        Args:
            id (number): id of the user

        Returns:
            JSON: All the informations of this same user 
        """
        update_filter = { "_id": ObjectId(current_user.id) }
        new_values = {
            "$set": {
                "username": "Removed User",
                "email": None,
                "password": None,
            }
        }

        self.db_users.update_one(update_filter, new_values)


users = CRUDUsers(next(get_db()))