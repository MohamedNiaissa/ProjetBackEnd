from fastapi import HTTPException
from pymongo.collection import Collection
from pymongo.database import Database

from api.v1.endpoints import likes
from api.deps import get_db
from core.config import settings

class CRUDLikes():
    db_likes: Collection

    def __init__(self, db: Database):
        self.db_likes = db.get_collection("likes")


    def get_by_post_id(self, id: str):
        """
        This function fetch the likes linked to the post chosen by its ID from the collection called likes

        Args:
            id (int): id of the like 

        Returns:
            JSON: infos of that like 
        """
        try:
            return {}
        except HTTPException:
            pass 

    def get_by_comment_id(self, id: str):
        """
        This function fetch the likes linked to the comment chosen by its ID from the collection called likes

        Args:
            id (int): id of the likes

        Returns:
            JSON: infos of that like 
        """
        try:
            return {}
        except HTTPException:
            pass 



    def manage_on_comment(self):
        """
        Insert true or false (wheter it is liked or not) and infos linked to the comment such as the commentID and userID

        Returns:
            JSON: all the infos of that like
        """
        try:
            return {}
        except HTTPException:
            pass 


    def manage_on_post(self):
        """
        Insert true or false (wheter it is liked or not) and infos linked to the post such as the postID and userID

        Returns:
            JSON: all the infos of that like
        """
        try:
            return {}
        except HTTPException:
            pass 


likes = CRUDLikes(next(get_db()))