from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_likes
from mongo.schemas.likes import *

router = APIRouter()


@router.get("/posts/{id}", response_model=LikeBase)
def get_likes_by_post_id():
    """
    Retrieve a specified like.
    """
    try:
        # return crud_likes.CRUD_likes.get_by_comment_id(id)
        return {}
    except HTTPException:
        pass 


@router.get("/comments/{id}",response_model=LikeBase)
def get_likes_by_comment_id():
    """
    Retrieve a like by using a specified comment.
    """
    try:
        # return crud_likes.CRUD_likes.get_by_comment_id(id)
        return {}
    except HTTPException:
        pass 


@router.post("/comments", response_model=LikeCreate)
@auth_guard("user")
def manage_like_on_comment(request: Request):
    """
    Create a like on a comment.
    """
    try:
        return crud_likes.CRUD_likes.manage_on_comment()
    except HTTPException:
        pass 


@router.post("/posts", response_model=LikeCreate)
@auth_guard("user")
def manage_like_on_post(request: Request):
    """
    Create a like on a post.
    """
    try:
        return crud_likes.CRUD_likes.manage_on_post()
    except HTTPException:
        pass 

