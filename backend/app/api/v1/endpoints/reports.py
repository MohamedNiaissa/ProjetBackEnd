from fastapi import APIRouter, HTTPException
from crud import crud_reports


router = APIRouter()


@router.get("/")
def get_report(id):
    try:
        return crud_reports.CRUD_reports.get(id)
    except HTTPException:
        pass 


@router.post("/")
def create_report():
    try:
        return crud_reports.CRUD_reports.create
    except HTTPException:
        pass 


@router.delete("/{id}")
def delete_report(id):
    try:
        return crud_reports.CRUD_reports.delete(id)
    except HTTPException:
        pass 