from fastapi import HTTPException
from pymongo.collection import Collection
from pymongo.database import Database

from api.v1.endpoints import users
from mongo.init_db import get_db
from mongo.schemas.users import UserCreate, UserInDB
from mongo.models.users import User
from bson import ObjectId

from core.security import (
	get_password_hash
)


class CRUDUsers():
    db_users: Collection

    def __init__(self, db: Database):
        self.db_users = db.get_collection("users")


    def exist(self, email: str) -> UserInDB | None:
        return self.db_users.find_one({
            "email": email,
        })


    def get(self, id: str) -> UserInDB | None:
        return self.db_users.find_one({
            "_id": ObjectId(id)
        })


    def create(self, user: UserCreate) -> User:
        """
        Create a user and insert it on the users collection

        Returns:
            JSON: inserted infos for the created user
        """
        new_user = User(
            username=user.username,
            email=user.email,
            password=get_password_hash(user.password),
        )
        new_user.__dict__.pop("id")
        res = self.db_users.insert_one(new_user.__dict__)
        new_user.id = res.inserted_id
        return new_user


    def get_all(self):
        """
        This function fetch all the users from the collection called users 

        Returns:
            JSON: informations of all users
        """
        try:
            return {}
        except HTTPException:
            pass 
    
    def get_by_id(self, id: str):
        """
        This function fetch the user chosen by its ID from the collection called users
        
        Args:
            id (number): id of the user
            
        Returns:
            JSON: informations of the choosen user
        """
        try:
            return {}
        except:
            pass

    def get_my(self):
        """
        This function fetch the current connected user from the collection called users
        Returns:
            JSON: informations of my user
        """
        try:
            return {}
        except:
            pass


    def modify(self, id: str):
        """
        Modify one or more specific data from a specific user

        Args:
            id (number): id of the user

        Returns:
            JSON: All the informations of this same user 
        """
        try:
            return {}
        except HTTPException:
            pass 

    def delete(self, id: str):
        """
        Delete a specific user

        Args:
            id (number): id of the user

        Returns:
            JSON: All the informations of this same user 
        """
        try:
            return {}
        except HTTPException:
            pass 


users = CRUDUsers(next(get_db()))