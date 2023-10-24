from database.db import SQLCursor
from database.queries import SQLQueries

from models.user import User

from utils.io_functions import credential_input
from utils.crypt import Crypt
from utils.show_message import show_message
from utils.helpers.exceptions import InvalidCredentials
# from utils.state_manager import StateManager

from sqlite3 import IntegrityError


class AuthenticationHandler:
    """
    Authentication Handler which provides sign up, sign in and sign out.
    """

    @staticmethod
    def sign_in(username = None, password = None):
        if not username or not password:
            username, password = credential_input()

        try:
            with SQLCursor() as cursor:
                user_data = cursor.execute(SQLQueries.SIGN_IN, (username,)).fetchone()

                if not user_data:
                    raise InvalidCredentials("Invalid username")

                hashed_password = user_data[2]

                if not Crypt.check(password, hashed_password):
                    raise InvalidCredentials("Invalid password!")

        except InvalidCredentials:
            # logging for invalid attempt
            raise
        else:
            return User.from_database(user_data)

    @staticmethod
    def sign_up(user_role: int):
        username, password = credential_input()
        password_hash = Crypt.hash(password)
        # del password

        try:
            with SQLCursor() as cursor:
                cursor.execute(SQLQueries.SIGN_UP, (username, password_hash, user_role))
        except IntegrityError:
            # logging for unique username
            raise
        else:
            return AuthenticationHandler.sign_in(username, password)

    @staticmethod
    def sign_out():
        ...
