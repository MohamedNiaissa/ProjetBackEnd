from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("posts/")
def getPosts():
    try:
        return {}
    except HTTPException:
        pass 

@router.get("posts/{id}")
def getPostById(id):
    try:
        return {}
    except HTTPException:
        pass 

@router.post("posts/")
def createPost():
    try:
        return {}
    except HTTPException:
        pass 

@router.patch("posts/{id}")
def modifyPost():
    try:
        return {}
    except HTTPException:
        pass 

@router.delete("posts/{id}")
def deletePost(id):
    try:
        return {}
    except HTTPException:
        pass 