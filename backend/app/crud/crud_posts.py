from mimetypes import init
from typing import Dict
from bson import ObjectId
from fastapi import HTTPException
from pymongo.collection import Collection
from pymongo.database import Database

from api.v1.endpoints import posts
from mongo.init_db import get_db
from core.config import settings
from pydantic import ValidationError

from fastapi import HTTPException, status



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


    def get_by_id(self, id):
        """
        This function fetch the post chosen by its ID from the collection called posts

        Args:
            id (int): id of the post

        Returns:
            JSON: all informations of the choosen post
        """
        try:
            objInstance = ObjectId(id)
            post = self.db_posts.find_one({"_id": objInstance})
            return post
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


    def modify(self, id: ObjectId, post_update: Dict):
        """
        Modify one or more specific data from a specific post
        
        Args:
             id (int): id of the post

        Returns:
            JSON: All the informations of this same post
        """
        try:
            objInstance = ObjectId(id)
            if "title" in post_update:
                my_post = { "_id": objInstance }
                new_title = { "$set": { "title": post_update["title"] } }
                self.db_posts.update_one(my_post, new_title)
            if "description" in post_update:
                    my_description = { "_id": objInstance }
                    new_description = { "$set": { "description": post_update["description"] } }
                    self.db_posts.update_one(my_description, new_description)
            else:
                raise HTTPException(
			    status_code=status.HTTP_400_BAD_REQUEST,
		    	detail="ERROR: You have not change anything ")
                
        except HTTPException:
            pass 


    def delete(self, id: str) -> None:
        """
        Delete a specific post     

        Args:
            id (int): id of the post

        Returns:
            JSON: All the informations of this same post
        """
        try:
            objInstance = ObjectId(id)
            count = self.db_posts.delete_one({"_id": objInstance})
            if count.deleted_count == 0:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Post does not exist"
                )
        except HTTPException:
            pass 


posts = CRUDPosts(next(get_db()))