from api.v1.endpoints import posts
from core.config import Settings
from fastapi import HTTPException

class CRUD_posts():
    
    def get_all():
        """
        This function fetch all the posts from the collection called posts

        Returns:
            JSON: informations of all posts
        """
        try:
            return {}
        except HTTPException:
            pass 


    def get_by_id(id):
        """
        This function fetch the post chosen by its ID from the collection called posts

        Args:
            id (int): id of the post

        Returns:
            JSON: all informations of the choosen post
        """
        try:
            return {}
        except HTTPException:
            pass 


    def create():
        """
        Create a post and insert it on the posts collection

        Returns:
            JSON: inserted data post
        """
        try:
            return {}
        except HTTPException:
            pass 


    def modify(id):
        """
        Modify one or more specific data from a specific post
        
        Args:
            id (int): id of the post

        Returns:
            JSON: All the informations of this same post
        """
        try:
            return {}
        except HTTPException:
            pass 


    def delete(id):
        """
        Delete a specific post     

        Args:
            id (int): id of the post

        Returns:
            JSON: All the informations of this same post
        """
        try:
            return {}
        except HTTPException:
            pass 
    
         