from fastapi import FastAPI
from app.routers import user_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Money Mate!"}

app.include_router(user_router.router)