from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("users/")
def getUsers():
    return {}

@app.get("users/{id}")
def getUserById(id):
    return {}

@app.get("users/me")
def getMyUser():
    return {}

@app.post("users/")
def createUser():
    return {}

@app.patch("users/{id}")
def modifyUser():
    return {}

@app.delete("users/{id}")
def deleteUser(id):
    return {}

