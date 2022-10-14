from typing import Any, List

from fastapi import APIRouter, HTTPException, Request
from api.deps import auth_guard
from crud import crud_reports
from mongo.schemas.reports import *

router = APIRouter()


@router.get("/", response_model=ReportBase)
@auth_guard("admin")
def get_report(request: Request):
    """
    Retrieve reports.
    """
    try:
        # return crud_reports.CRUD_reports.get()

        print(request)
        print(request.attach_user)
        return {"success": True}
    except HTTPException:
        pass


@router.post("/", response_model=ReportBase)
@auth_guard("user")
def create_report(request: Request):
    """
    Create new report.
    """
    try:
        return crud_reports.CRUD_reports.create()
    except HTTPException:
        pass


@router.delete("/{id}")
@auth_guard("admin")
def delete_report(request: Request):
    """
    Delete a specified report.
    """
    try:
        # return crud_reports.CRUD_reports.delete(id)
        print(request.attach_user)
        return {"Status": "200 OK"}
    except HTTPException:
        pass
