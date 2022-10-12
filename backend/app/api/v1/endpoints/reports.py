from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/")
def get_report():
    try:
        return {}
    except HTTPException:
        pass 

@router.post("/")
def create_report():
    try:
        return {}
    except HTTPException:
        pass 

@router.delete("/{id}")
def delete_report(id):
    try:
        return {}
    except HTTPException:
        pass 