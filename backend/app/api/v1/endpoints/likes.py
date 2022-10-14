from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_likes

router = APIRouter()


@router.get("/posts/{id}")
def get_likes_by_post_id():
    """
    Gets like status from a specified post

    Args:
        string (id): id of the post to get status from

    Raises:
        HTTPException: raise 404 if no likes were found or if no posts were found

    Returns:
        JSON : infos of that like
    """
    try:
        # return crud_likes.CRUD_likes.get_by_comment_id(id)
        return {}
    except HTTPException:
        pass 


@router.get("/comments/{id}")
def get_likes_by_comment_id():
    """
    Gets like status from a specified comment

    Args:
        string (id): id of the comment to get status from

    Raises:
        HTTPException: raise 404 if no likes were found or if no comments were found

    Returns:
        JSON : infos of that like
    """
    try:
        # return crud_likes.CRUD_likes.get_by_comment_id(id)
        return {}
    except HTTPException:
        pass 


@router.post("/comments")
@auth_guard("user")
def manage_like_on_comment(request: Request):
    """
    Changes the status of the like and infos linked to the comment such as the commentID and userID

    Args:
        request (Request): comment details are linked to it

    Raises:
        HTTPException: raise 404 if no comment is found

    Returns:
        JSON: all the infos of that like
    """
    try:
        return crud_likes.CRUD_likes.manage_on_comment()
    except HTTPException:
        pass 


@router.post("/posts")
@auth_guard("user")
def manage_like_on_post(request: Request):
    """
    Changes the status of the like and infos linked to the comment such as the commentID and userID

    Args:
        request (Request): comment details are linked to it

    Raises:
        HTTPException: raise 404 if no comment is found

    Returns:
        JSON: all the infos of that like
    """
    try:
        return crud_likes.CRUD_likes.manage_on_post()
    except HTTPException:
        pass 

