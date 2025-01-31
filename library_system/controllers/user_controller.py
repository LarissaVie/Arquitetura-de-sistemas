from fastapi import APIRouter, HTTPException
from models.user import User
from services.user_service import UserService

router = APIRouter()

@router.get("/users")
def get_all_users():
    return UserService.get_all_users()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = UserService.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/users")
def add_user(user: User):
    UserService.add_user(user)
    return {"message": "User added successfully"}

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    UserService.delete_user(user_id)
    return {"message": "User deleted successfully"}