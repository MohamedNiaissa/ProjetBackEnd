from mimetypes import init
from fastapi import HTTPException
from pymongo.collection import Collection
from pymongo.database import Database

from api.v1.endpoints import posts
from api.deps import get_db
from core.config import settings

class CRUDPosts():
    db_posts: Collection

    def __init__(self, db: Database):
        self.db_posts = db.get_collection("posts")


    def get_all(self):
        """
        This function fetch all the posts from the collection called posts

        Returns:
            JSON: informations of all posts
        """
        try:
            post = list(self.db_posts.find())
            return post
        except HTTPException:
            pass 


    def get_by_id(self, id: str):
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


    def create(self,post):
        """
        Create a post and insert it on the posts collection

        Returns:
            JSON: inserted data post
        """
        try:
            return self.db_posts.insert_one(post)
        except HTTPException:
            pass 


    def modify(self, id: str):
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


    def delete(self, id: str):
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


posts = CRUDPosts(next(get_db()))