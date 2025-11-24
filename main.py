# FastAPI 기본 구현
from fastapi import FastAPI

app = FastAPI()

# http://localhost:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

pass