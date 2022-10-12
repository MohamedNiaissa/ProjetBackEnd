from typing import Any, List

from fastapi import APIRouter
from crud import crud_users
from fastapi.encoders import jsonable_encoder


router = APIRouter()


@router.get("/")
def get_users(): 
    crud_users.CRUDUser.get_all


@router.get("/{id}")
def get_user_by_id(id):
    crud_users.CRUDUser.get_by_id(id)


@router.get("/me")
def get_my_user():
    crud_users.CRUDUser.get_my


@router.post("/")
def create_user():
    crud_users.CRUDUser.create


@router.patch("/{id}")
def modify_user(id):
    crud_users.CRUDUser.modify(id)


@router.delete("/{id}")
def delete_user(id):
    crud_users.CRUDUser.delete(id)