from fastapi import HTTPException
from pymongo.collection import Collection
from pymongo.database import Database

from api.v1.endpoints import comments
from api.deps import get_db
from core.config import settings

class CRUDComments():
    db_comments: Collection

    def __init__(self, db: Database):
        self.db_comments = db.get_collection("comments")


    def get_all(self):
        """
        This function fetch all the comments from the collection called comments

        Returns:
            JSON: informations of all comments
        """
        try:
            return {}
        except HTTPException:
            pass 

    def get_by_id(self, id: str):
        """
        This function fetch the comment chosen by its ID from the collection called comments

        Args:
            id (int): id of the comment

        Returns:
            JSON: all informations of the choosen comment
        """
        try:
            return {}
        except HTTPException:
            pass 

    def create(self, id: str):
        """
        Create a comment and insert it on the comments collection

        Returns:
            JSON: inserted data comment
        """
        try:
            return {}
        except HTTPException:
            pass 

    def modify(self, id: str):
        """
        Modify one or more specific data from a specific comment
        
        Args:
            id (int): id of the comment

        Returns:
            JSON: All the informations of this same comment
        """
        try:
            return {}
        except HTTPException:
            pass 

    def delete(self, id: str):
        """
        Delete a specific comment     

        Args:
            id (int): id of the comment

        Returns:
            JSON: All the informations of this same comment
        """
        try:
            return {}
        except HTTPException:
            pass 


comments = CRUDComments(next(get_db()))