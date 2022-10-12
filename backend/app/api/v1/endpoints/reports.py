from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("reports/")
def getReport():
    try:
        return {}
    except HTTPException:
        pass 

@router.post("reports/")
def createReport():
    try:
        return {}
    except HTTPException:
        pass 

@router.delete("reports/{id}")
def deleteReport(id):
    try:
        return {}
    except HTTPException:
        pass 