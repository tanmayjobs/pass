from database.db import SQLCursor, SQLQueries

from utils.helpers.enums import UserType
from utils.helpers.exceptions import InvalidCredentials
from utils.crypt import Crypt


class User:
    """
    User model which contains all the user's public details.
    """

    def __init__(self, user_id: int, user_type: UserType, username: str) -> None:
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
        with SQLCursor() as cursor:
            user_data = cursor.execute(SQLQueries.SIGN_IN, (username,)).fetchone()

            if not user_data:
                raise InvalidCredentials("Invalid username")

            hashed_password = user_data[2]

            if not Crypt.check(password, hashed_password):
                raise InvalidCredentials("Invalid password!")

        return User.from_database(user_data)

    @staticmethod
    def sign_up(username, password_hash, user_role):
        with SQLCursor() as cursor:
            cursor.execute(SQLQueries.SIGN_UP, (username, password_hash, user_role))
