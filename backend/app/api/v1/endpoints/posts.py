from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/")
def get_posts():
    try:
        return {}
    except HTTPException:
        pass 


@router.get("/{id}")
def get_post_by_id(id):
    try:
        return {}
    except HTTPException:
        pass 


@router.post("/")
def create_post():
    try:
        return {}
    except HTTPException:
        pass 


@router.patch("/{id}")
def modify_post():
    try:
        return {}
    except HTTPException:
        pass 


@router.delete("/{id}")
def delete_post(id):
    try:
        return {}
    except HTTPException:
        pass 