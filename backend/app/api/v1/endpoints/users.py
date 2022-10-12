from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/")
def get_users():
    try:
        return {}
    except HTTPException:
        pass 


@router.get("/{id}")
def get_user_by_id(id):
    try:
        return {}
    except HTTPException:
        pass 


@router.get("/me")
def get_my_user():
    try:
        return {}
    except HTTPException:
        pass 


@router.post("/")
def create_user():
    try:
        return {}
    except HTTPException:
        pass 


@router.patch("/{id}")
def modify_user():
    try:
        return {}
    except HTTPException:
        pass 


@router.delete("/{id}")
def delete_user(id):
    try:
        return {}
    except HTTPException:
        pass 