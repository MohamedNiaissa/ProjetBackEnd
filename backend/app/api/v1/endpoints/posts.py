from json import dumps
from turtle import pos
from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_posts
from mongo.schemas.posts import *

router = APIRouter()

@router.get("/", response_model=List[PostBase])
def get_posts():
    """
    Retrieve posts.
    """
    try:
        posts = crud_posts.posts.get_all()
        return posts
    except HTTPException:
        pass


@router.get("/{id}", response_model=PostBase)
def get_post_by_id(id):
	try:
		return crud_posts.posts.get_by_id(id)
	except HTTPException:
		pass 


@router.post("/", response_model=PostBase)
#@auth_guard("user")
def create_post(request: Request, post : PostBase):
    try:
        post = crud_posts.posts.create(post.__dict__)
        print("^^^^^^^^^^^^^^^^^^^^^^")
        print(post)
        print("^^^^^^^^^^^^^^^^^^^^^^")
        return post
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
