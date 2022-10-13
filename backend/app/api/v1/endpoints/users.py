from typing import Any, List

from fastapi import APIRouter, HTTPException
from api.deps import auth_guard
from crud import crud_users


router = APIRouter()


@router.get("/")
@auth_guard("admin")
def get_users(): 
    try:
        crud_users.CRUD_users.get_all
    except HTTPException:
        pass


@router.get("/{id}")
@auth_guard("admin")
def get_user_by_id(id):
    try:
        crud_users.CRUD_users.get_by_id(id)
    except HTTPException:
        pass


@router.get("/me")
@auth_guard("user")
def get_my_user():
    try:
        crud_users.CRUD_users.get_my
    except HTTPException:
        pass


@router.post("/")
def create_user():
    try:
        crud_users.CRUD_users.create
    except HTTPException:
        pass


@router.patch("/{id}")
@auth_guard("user")
def modify_user(id):
    try:
        crud_users.CRUD_users.modify(id)
    except HTTPException:
        pass


@router.delete("/{id}")
@auth_guard("user")
def delete_user(id):
    try:
        crud_users.CRUD_users.delete(id)
    except HTTPException:
        pass