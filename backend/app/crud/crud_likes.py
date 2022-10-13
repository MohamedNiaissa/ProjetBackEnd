from api.v1.endpoints import posts
from core.config import Settings
from fastapi import HTTPException

class CRUD_likes():
    def get_by_post_id(id):
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

    def get_by_comment_id(id):
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



    def manage_on_comment():
        """
        Insert true or false (wheter it is liked or not) and infos linked to the comment such as the commentID and userID

        Returns:
            JSON: all the infos of that like
        """
        try:
            return {}
        except HTTPException:
            pass 


    def manage_on_post():
        """
        Insert true or false (wheter it is liked or not) and infos linked to the post such as the postID and userID

        Returns:
            JSON: all the infos of that like
        """
        try:
            return {}
        except HTTPException:
            pass 

