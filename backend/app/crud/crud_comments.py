from api.v1.endpoints import posts
from core.config import Settings
from fastapi import HTTPException

class CRUD_comments():
    
    def get_all():
        """
        This function fetch all the comments from the collection called comments

        Returns:
            JSON: informations of all comments
        """
        try:
            return {}
        except HTTPException:
            pass 

    def get_by_id(id):
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

    def create():
        """
        Create a comment and insert it on the comments collection

        Returns:
            JSON: inserted data comment
        """
        try:
            return {}
        except HTTPException:
            pass 

    def modify():
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

    def delete(id):
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
