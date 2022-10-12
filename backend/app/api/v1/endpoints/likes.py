from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/posts/{id}")
def get_likes_for_post_by_id(id):
    try:
        return {}
    except HTTPException:
        pass 

@router.get("/comments/{id}")
def get_likes_for_comment_by_id(id):
    try:
        return {}
    except HTTPException:
        pass 

@router.post("/comments")
def like_comment():
    try:
        return {}
    except HTTPException:
        pass 

@router.post("/posts")
def like_post():
    try:
        return {}
    except HTTPException:
        pass 

