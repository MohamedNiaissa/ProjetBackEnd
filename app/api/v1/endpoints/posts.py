from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("posts/")
def getPosts():
    return {}

@app.get("posts/{id}")
def getPostById(id):
    return {}

@app.post("posts/")
def createPost():
    return {}

@app.patch("posts/{id}")
def modifyPost():
    return {}

@app.delete("posts/{id}")
def deletePost(id):
    return {}

