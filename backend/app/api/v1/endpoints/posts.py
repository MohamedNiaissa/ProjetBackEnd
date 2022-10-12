from typing import Any, List
from fastapi import APIRouter, HTTPException
from crud import crud_posts


router = APIRouter()


@router.get("/")
def get_posts():
    try:
        return crud_posts.CRUD_posts.get_all
    except HTTPException:
        pass 


@router.get("/{id}")
def get_post_by_id(id):
    try:
        return crud_posts.CRUD_posts.get_by_id(id)
    except HTTPException:
        pass 


@router.post("/")
def create_post():
    try:
        return crud_posts.CRUD_posts.create
    except HTTPException:
        pass 


@router.patch("/{id}")
def modify_post():
    try:
        return crud_posts.CRUD_posts.modify(id)
    except HTTPException:
        pass 


@router.delete("/{id}")
def delete_post(id):
    try:
        return crud_posts.CRUD_posts.delete(id)
    except HTTPException:
        pass 