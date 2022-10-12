from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("reports/")
def getReport():
    return {}

@app.post("reports/")
def createReport():
    return {}

@app.delete("reports/{id}")
def deleteReport(id):
    return {}

