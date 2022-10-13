from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_reports

router = APIRouter()


@router.get("/")
@auth_guard("admin")
def get_report(request: Request):
    try:
        print(request)
        print(request.attach_user)
        return { "sucess": True }
    except HTTPException:
        pass 


@router.post("/")
@auth_guard("user")
def create_report():
    try:
        return crud_reports.CRUD_reports.create
    except HTTPException:
        pass 


@router.delete("/{id}")
@auth_guard("admin")
def delete_report(id):
    try:
        return crud_reports.CRUD_reports.delete(id)
    except HTTPException:
        pass 