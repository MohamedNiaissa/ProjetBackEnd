from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("likes/posts/{id}")
def getLikesForPostById(id):
    return {}

@app.get("likes/comments/{id}")
def getLikesForCommentById(id):
    return {}

@app.post("likes/comments")
def likeComment():
    return {}

@app.post("likes/posts")
def likePost():
    return {}



