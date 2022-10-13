from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_posts

router = APIRouter()


@router.get("/")
def get_posts():
    """
    Retrieve posts.
    """
    try:
        return crud_posts.CRUD_posts.get_all()
    except HTTPException:
        pass


@router.get("/{id}")
def get_post_by_id():
    """
    Retrieve specified post.
    """
    try:
        # return crud_posts.CRUD_posts.get_by_id(id)
        return {}
    except HTTPException:
        pass


@router.post("/")
@auth_guard("user")
def create_post(request: Request):
    """
    Create new post.
    """
    try:
        return crud_posts.CRUD_posts.create()
    except HTTPException:
        pass


@router.patch("/{id}")
@auth_guard("user")
def modify_post(request: Request):
    """
    Update a specified post.
    """
    try:
        # return crud_posts.CRUD_posts.modify(id)
        print(request.attach_user)
    except HTTPException:
        pass


@router.delete("/{id}")
@auth_guard("user")
def delete_post(request: Request):
    """
    Delete specified post.
    """
    try:
        # return crud_posts.CRUD_posts.delete(id)
        print(request.attach_user)
    except HTTPException:
        pass
