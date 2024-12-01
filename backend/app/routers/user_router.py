from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def get_user():
    return {"message": "User information endpoint"}