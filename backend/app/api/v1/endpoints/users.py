from typing import Any, List

from fastapi import APIRouter, HTTPException
from crud import crud_users
from fastapi.encoders import jsonable_encoder


router = APIRouter()


@router.get("/")
def get_users(): 
    try:
        crud_users.CRUD_users.get_all()
        return {"users" : "user", "use":"use"}
    except HTTPException:
        pass

    

@router.get("/me")
def get_my_user():
    try:
        crud_users.CRUD_users.get_my()
    except HTTPException:
        pass



@router.get("/{id}")
def get_user_by_id(id):
    try:
        crud_users.CRUD_users.get_by_id(id)
    except HTTPException:
        pass


@router.post("/")
def create_user():
    try:
        crud_users.CRUD_users.create()
    except HTTPException:
        pass


@router.patch("/{id}")
def modify_user(id):
    try:
        crud_users.CRUD_users.modify(id)
    except HTTPException:
        pass


@router.delete("/{id}")
def delete_user(id):
    try:
        crud_users.CRUD_users.delete(id)
    except HTTPException:
        pass