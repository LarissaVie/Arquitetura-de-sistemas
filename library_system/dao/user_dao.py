from typing import List
from models.user import User

users = []

class UserDAO:
    @staticmethod
    def get_all_users() -> List[User]:
        return users

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        for user in users:
            if user.id == user_id:
                return user
        return None

    @staticmethod
    def add_user(user: User):
        users.append(user)

    @staticmethod
    def delete_user(user_id: int):
        global users
        users = [user for user in users if user.id != user_id]