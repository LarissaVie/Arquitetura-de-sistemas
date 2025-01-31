from dao.user_dao import UserDAO
from models.user import User

class UserService:
    @staticmethod
    def get_all_users():
        return UserDAO.get_all_users()

    @staticmethod
    def get_user_by_id(user_id: int):
        return UserDAO.get_user_by_id(user_id)

    @staticmethod
    def add_user(user: User):
        UserDAO.add_user(user)

    @staticmethod
    def delete_user(user_id: int):
        UserDAO.delete_user(user_id)