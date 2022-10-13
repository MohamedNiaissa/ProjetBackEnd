from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_users


router = APIRouter()


@router.get("/")
@auth_guard("admin")
def get_users(request: Request): 
    try:
        crud_users.CRUD_users.get_all()
        return {"users" : "user", "use":"use"}
    except HTTPException:
        pass

    

@router.get("/me")
@auth_guard("user")
def get_my_user(request: Request):
    try:
        crud_users.CRUD_users.get_my()
    except HTTPException:
        pass


@router.get("/{id}")
@auth_guard("user")
def get_user_by_id(request: Request):
	try:
		# crud_users.CRUD_users.get_by_id(id)
		print(request.attach_user)
	except HTTPException:
		pass


@router.post("/")
def create_user(request: Request):
    try:
        crud_users.CRUD_users.create()
    except HTTPException:
        pass


@router.patch("/{id}")
@auth_guard("user")
def modify_user(request: Request):
	try:
		# crud_users.CRUD_users.modify(id)
		print(request.attach_user)
	except HTTPException:
		pass


@router.delete("/{id}")
@auth_guard("user")
def delete_user(request: Request):
	try:
		# crud_users.CRUD_users.delete(id)
		print(request.attach_user)
	except HTTPException:
		pass