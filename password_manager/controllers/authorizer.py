"""
This file contains the controller for authentication.
Sign In, Sign Up for authentication are defined in this file.
"""

from logs.logger import Logger, WARN, INFO

from models.user import User

from utils.io_functions import credential_input
from utils.crypt import Crypt
from utils.helpers.exceptions import InvalidCredentials

from sqlite3 import IntegrityError


class Authorizer:
    """
    Authentication Handler which provides sign up, sign in and sign out.
    """

    @staticmethod
    def sign_in(username=None, password=None):
        if not username or not password:
            username, password = credential_input()

        try:
            user = User.sign_in(username, password)
        except InvalidCredentials:
            Logger.log(WARN, f"Invalid Credentials by {username}.")
            raise
        else:
            return user

    @staticmethod
    def sign_up(user_role: int):
        username, password = credential_input(check_strength=True)
        password_hash = Crypt.hash(password)

        try:
            User.sign_up(username, password_hash, user_role)
        except IntegrityError:
            Logger.log(WARN, f"Duplicate account creation attempt {username}.")
            raise
        else:
            return

    @staticmethod
    def sign_out():
        Logger.log(INFO, f"User signed out.")
