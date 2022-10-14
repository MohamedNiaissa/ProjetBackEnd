from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_comments
from mongo.schemas.comments import *

router = APIRouter()


@router.get("/", response_model=Comment)
def get_comments():
    """
	Retrieve comments.
    """
    try:
        return crud_comments.CRUD_comments.get_all()
    except HTTPException:
        pass


@router.post("/", response_model=CommentCreate)
@auth_guard("user")
def create_comment(request: Request):
    """
    Create a comment.
    """
    try:
        return crud_comments.CRUD_comments.create()
    except HTTPException:
        pass


@router.patch("/{id}", response_model=CommentUpdate)
@auth_guard("user")
def modify_comment(request: Request):
    """
    Update a comment.
    """
    try:
        # return crud_comments.CRUD_comments.modify(id)
        print(request.attach_user)
    except HTTPException:
        pass


@router.delete("/{id}")
@auth_guard("user")
def delete_comment(request: Request):
    """
    Delete a comment.
    """
    try:
        # return crud_comments.CRUD_comments.delete(id)
        print(request.attach_user)
        return {"Status": "200 OK"}
    except HTTPException:
        pass
