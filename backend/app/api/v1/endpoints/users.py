from typing import Any, List

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("users/")
def getUsers():
    try:
        return {}
    except HTTPException:
        pass 

@router.get("users/{id}")
def getUserById(id):
    try:
        return {}
    except HTTPException:
        pass 

@router.get("users/me")
def getMyUser():
    try:
        return {}
    except HTTPException:
        pass 

@router.post("users/")
def createUser():
    try:
        return {}
    except HTTPException:
        pass 

@router.patch("users/{id}")
def modifyUser():
    try:
        return {}
    except HTTPException:
        pass 

@router.delete("users/{id}")
def deleteUser(id):
    try:
        return {}
    except HTTPException:
        pass 