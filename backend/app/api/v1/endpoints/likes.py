from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("likes/posts/{id}")
def getLikesForPostById(id):
    try:
        return {}
    except HTTPException:
        pass 

@router.get("likes/comments/{id}")
def getLikesForCommentById(id):
    try:
        return {}
    except HTTPException:
        pass 

@router.post("likes/comments")
def likeComment():
    try:
        return {}
    except HTTPException:
        pass 

@router.post("likes/posts")
def likePost():
    try:
        return {}
    except HTTPException:
        pass 

