from typing import Any, List

from fastapi import APIRouter, HTTPException
from crud import crud_comments


router = APIRouter()


@router.get("/")
def get():
    try:
        return crud_comments.CRUD_comments.get_all
    except HTTPException:
        pass 


@router.get("/{id}")
def get_by_id(id):
    try:
        return crud_comments.CRUD_comments.get_by_id(id)
    except HTTPException:
        pass 


@router.post("/")
def create():
    try:
        return crud_comments.CRUD_comments.create
    except HTTPException:
        pass 


@router.patch("/{id}")
def modify():
    try:
        return crud_comments.CRUD_comments.modify(id)
    except HTTPException:
        pass 


@router.delete("/{id}")
def delete(id):
    try:
        return crud_comments.CRUD_comments.delete(id)
    except HTTPException:
        pass 
