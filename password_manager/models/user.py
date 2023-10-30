"""
This file contains the User Model.
User Model is created for each user.
User Model is capable of accessing the Database to perform CRUD operation related to users.
"""

from database.db import SQLDatabase, SQLQueries

from utils.helpers.enums import UserType
from utils.helpers.exceptions import InvalidCredentials
from utils.crypt import Crypt


class User:
    """
    User model which contains all the user's public details.
    """

    def __init__(self, user_id: int, user_type: UserType,
                 username: str) -> None:
        self.user_id = user_id
        self.user_type = UserType(user_type)
        self.username = username

    @staticmethod
    def from_database(user_data: tuple):
        return User(
            user_id=user_data[0],
            user_type=user_data[3],
            username=user_data[1],
        )

    def __repr__(self) -> str:
        return f"{self.username:20}"

    @staticmethod
    def sign_in(username, password):
        db = SQLDatabase()
        user_data = db.get(SQLQueries.SIGN_IN, (username, ))

        if not user_data:
            raise InvalidCredentials("Invalid username")

        user_data = user_data[0]
        hashed_password = user_data[2]

        if not Crypt.check(password, hashed_password):
            raise InvalidCredentials("Invalid password!")

        return User.from_database(user_data)

    @staticmethod
    def sign_up(username, password_hash, user_role):
        db = SQLDatabase()
        db.add(SQLQueries.SIGN_UP, (username, password_hash, user_role))
