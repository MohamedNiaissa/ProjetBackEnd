from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("comments/")
def getComments():
    try:
        return {}
    except HTTPException:
        pass 

@router.get("comments/{id}")
def getCommentById(id):
    try:
        return {}
    except HTTPException:
        pass 

@router.post("comments/")
def createComment():
    try:
        return {}
    except HTTPException:
        pass 

@router.patch("comments/{id}")
def modifyComment():
    try:
        return {}
    except HTTPException:
        pass 

@router.delete("comments/{id}")
def deleteComment(id):
    try:
        return {}
    except HTTPException:
        pass 
