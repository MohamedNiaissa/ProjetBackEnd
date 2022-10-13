from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_likes

router = APIRouter()


@router.get("/posts/{id}")
def get_likes_by_post_id():
    try:
        # return crud_likes.CRUD_likes.get_by_comment_id(id)
        return {}
    except HTTPException:
        pass 


@router.get("/comments/{id}")
def get_likes_by_comment_id():
    try:
        # return crud_likes.CRUD_likes.get_by_comment_id(id)
        return {}
    except HTTPException:
        pass 


@router.post("/comments")
@auth_guard("user")
def manage_like_on_comment(request: Request):
    try:
        return crud_likes.CRUD_likes.manage_on_comment()
    except HTTPException:
        pass 


@router.post("/posts")
@auth_guard("user")
def manage_like_on_post(request: Request):
    try:
        return crud_likes.CRUD_likes.manage_on_post()
    except HTTPException:
        pass 

