from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_users

from mongo.models.users import UserBase
router = APIRouter()


@router.get("/")
#@auth_guard("admin")
def get_users(): 
    try:
        crud_users.users.get_all()
        return {"users" : "user", "use":"use"}
    except HTTPException:
        pass

    

@router.get("/me")
@auth_guard("user")
def get_my_user(request: Request):
    try:
        crud_users.users.get_my()
    except HTTPException:
        pass


@router.get("/{id}")
@auth_guard("user")
def get_user_by_id(request: Request):
	try:
		crud_users.users.get_by_id(id)
		print(request.attach_user)
	except HTTPException:
		pass


@router.post("/")
def create_user(request: Request, user : UserBase):
    try:
        crud_users.users.create(user)
    except HTTPException:
        pass


@router.patch("/{id}")
@auth_guard("user")
def modify_user(request: Request):
	try:
		print(request.attach_user)
		crud_users.users.modify(id)
	except HTTPException:
		pass


@router.delete("/{id}")
@auth_guard("user")
def delete_user(request: Request):
	try:
		crud_users.users.delete(id)
		print(request.attach_user)
	except HTTPException:
		pass