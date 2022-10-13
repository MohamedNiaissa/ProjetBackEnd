from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_comments


router = APIRouter()


@router.get("/")
def get_comments():
    try:
        return crud_comments.CRUD_comments.get_all
    except HTTPException:
        pass 


@router.post("/")
@auth_guard("user")
def create_comment(request: Request):
    try:
        return crud_comments.CRUD_comments.create
    except HTTPException:
        pass 


@router.patch("/{id}")
@auth_guard("user")
def modify_comment(request: Request):
	try:
		# return crud_comments.CRUD_comments.modify(id)
		print(request.attach_user)
	except HTTPException:
		pass 


@router.delete("/{id}")
@auth_guard("user")
def delete_comment(request: Request):
	try:
		# return crud_comments.CRUD_comments.delete(id)
		print(request.attach_user)
	except HTTPException:
		pass 
