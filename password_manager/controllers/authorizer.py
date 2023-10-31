"""
This file contains the controller for authentication.
Sign In, Sign Up for authentication are defined in this file.
"""

from sqlite3 import IntegrityError

from utils.crypt import Crypt
from helpers.exceptions import InvalidCredentials
from models.user import User
from logs.logger import Logger, WARN, INFO


def sign_in(username, password):
    try:
        user = User.sign_in(username, password)
    except InvalidCredentials:
        Logger.log(WARN, f"Invalid Credentials by {username}.")
        raise
    else:
        return user


def sign_up(username, password, user_role: int):
    password_hash = Crypt.hash(password)
    try:
        User.sign_up(username, password_hash, user_role)
    except IntegrityError:
        Logger.log(WARN, f"Duplicate account creation attempt {username}.")
        raise
    else:
        return


def sign_out():
    Logger.log(INFO, f"User signed out.")
