from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("comments/")
def getComments():
    return {}

@app.get("comments/{id}")
def getCommentById(id):
    return {}

@app.post("comments/")
def createComment():
    return {}

@app.patch("comments/{id}")
def modifyComment():
    return {}

@app.delete("comments/{id}")
def deleteComment(id):
    return {}

