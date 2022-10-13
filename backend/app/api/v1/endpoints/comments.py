from typing import Any, List

from fastapi import APIRouter, HTTPException
from crud import crud_comments


router = APIRouter()


@router.get("/")
def get_comments():
    try:
        return crud_comments.CRUD_comments.get_all()
    except HTTPException:
        pass 


@router.get("/{id}")
def get_comment_by_id(id):
    try:
        return crud_comments.CRUD_comments.get_by_id(id)
    except HTTPException:
        pass 


@router.post("/")
def create_comment():
    try:
        return crud_comments.CRUD_comments.create()
    except HTTPException:
        pass 


@router.patch("/{id}")
def modify_comment():
    try:
        return crud_comments.CRUD_comments.modify(id)
    except HTTPException:
        pass 


@router.delete("/{id}")
def delete_comment(id):
    try:
        return crud_comments.CRUD_comments.delete(id)
    except HTTPException:
        pass 
