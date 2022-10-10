from fastapi import FastAPI

app = FastAPI()

file_path = "/f/f.txt"

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
