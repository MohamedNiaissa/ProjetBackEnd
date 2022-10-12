from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/posts/{id}")
def get_likes_by_post_id(id):
    try:
        return {}
    except HTTPException:
        pass 


@router.get("/comments/{id}")
def get_likes_by_comment_id(id):
    try:
        return {}
    except HTTPException:
        pass 


@router.post("/comments")
def manage_like_on_comment():
    try:
        return {}
    except HTTPException:
        pass 


@router.post("/posts")
def manage_like_on_post():
    try:
        return {}
    except HTTPException:
        pass 

