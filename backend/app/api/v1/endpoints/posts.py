from json import dumps
from turtle import pos
from typing import Any, List
from bson import ObjectId

from fastapi import APIRouter, HTTPException, Request, Body
from api.deps import auth_guard
from crud import crud_posts
from mongo.schemas.posts import *

router = APIRouter()


@router.get("/", response_model=List[PostBase])
def get_posts(): 
    """
    Retrieve posts.

    Returns:
        JSON: return all posts
    """
    try:
        posts = crud_posts.posts.get_all()
        return posts
    except HTTPException:
        pass


@router.get("/{id}", response_model=PostBase)
def get_post_by_id(id): 
    """
    Retrieve a post by its id

    Args:
        id (int): id of this post

    Returns:
        JSON: return the data of that post 
    """
    try:
        return crud_posts.posts.get_by_id(id)
    except HTTPException:
        pass 


@router.post("/", response_model=PostCreate)
@auth_guard("user")
def create_post(request: Request, post : PostBase): #marche
    """
    Insert a post in the database

    Args:
        request (Request): necessary for auth_guard
        post (PostBase): infos of the post

    Returns:
        JSON: data of the created post
    """
    try:
        crud_posts.posts.create(post.__dict__)
        return  post.__dict__
    except HTTPException:
        pass


@router.patch("/{id}",response_model=PostUpdate)
@auth_guard("user")
def modify_post(request: Request, id: str, post_update = Body(...)): 
    """   
    Update a specified post by its id
    Args:
        request (Request): necessary for auth_guard
        id (str): id of the post
        post_update (_type_, optional): body where we update the title and/or the description.

    Returns:
        JSON: data of the post with modified fields
    """
    try:
        crud_posts.posts.modify(id, post_update)
        return post_update
    except HTTPException:
        pass


@router.delete("/{id}")
@auth_guard("user")
def delete_post(request: Request, id):
    """
    Delete specified post

    Args:
        request (Request): necessary for auth_guard
        id (int): _description_

    Returns:
        JSON: message "post deleted"
    """
    try:
        crud_posts.posts.delete(id) 
        return { "status": "OK" }
    except HTTPException:
        pass
