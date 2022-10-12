from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
def get_comments():
    try:
        return {}
    except HTTPException:
        pass 

@router.get("/{id}")
def get_commentById(id):
    try:
        return {}
    except HTTPException:
        pass 

@router.post("/")
def create_comment():
    try:
        return {}
    except HTTPException:
        pass 

@router.patch("/{id}")
def modify_comment():
    try:
        return {}
    except HTTPException:
        pass 

@router.delete("/{id}")
def delete_comment(id):
    try:
        return {}
    except HTTPException:
        pass 
