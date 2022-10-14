from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_users
from mongo.schemas.users import *

router = APIRouter()


@router.get("/", response_model=User)
@auth_guard("admin")
def get_users(request: Request):
    """
    Retrieve users.
    """
    try:
        crud_users.CRUD_users.get_all()
        return {"users": "user", "use": "use"}
    except HTTPException:
        pass


@router.get("/me", response_model=User)
@auth_guard("user")
def get_my_user(request: Request):
    """
    Retrieve own user.
    """
    try:
        crud_users.CRUD_users.get_my()
    except HTTPException:
        pass


@router.get("/{id}", response_model=User)
@auth_guard("user")
def get_user_by_id(request: Request):
    """
    Retrieve a specified user.
    """
    try:
        # crud_users.CRUD_users.get_by_id(id)
        print(request.attach_user)
    except HTTPException:
        pass


@router.post("/", response_model=UserCreate)
def create_user(request: Request):
    """
    Create a new user.
    """
    try:
        crud_users.CRUD_users.create()
    except HTTPException:
        pass


@router.patch("/{id}", response_model=UserUpdate)
@auth_guard("user")
def modify_user(request: Request):
    """
    Update a user.
    """
    try:
        # crud_users.CRUD_users.modify(id)
        print(request.attach_user)
    except HTTPException:
        pass


@router.delete("/{id}")
@auth_guard("user")
def delete_user(request: Request):
    """
    Delete a user.
    """
    try:
        # crud_users.CRUD_users.delete(id)
        print(request.attach_user)
        return {"Status": "OK"}
    except HTTPException:
        pass
