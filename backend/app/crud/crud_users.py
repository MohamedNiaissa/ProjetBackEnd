from fastapi import HTTPException
from pymongo.collection import Collection
from pymongo.database import Database

from api.v1.endpoints import users
from api.deps import get_db
from core.config import settings

class CRUDUsers():
    db_users: Collection

    def __init__(self, db: Database):
        self.db_users = db.get_collection("users")


    def get_all(self):
        """
        This function fetch all the users from the collection called users 

        Returns:
            JSON: informations of all users
        """
        try:
            users = self.db_users.find({})                
            return users
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

    def create(self,user):
        """
        Create a user and insert it on the users collection

        Returns:
            JSON: inserted infos for the created user
        """
        try:
            # user = {
            #     "username" : user.username,
            #     "email": user.email,
            #     "password": user.password,
            #     "token" : user.token,
            #     "salt" : user.salt,
            #     "refresh_token" : user.refresh_token
            # }
            return self.db_users.insert_one(user)
        except HTTPException:
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