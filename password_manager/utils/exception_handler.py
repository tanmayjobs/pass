"""
This file defines a decorator for functions which handles the menus.
Here all the exceptions(custom exceptions as well) are handled.
"""

from sqlite3 import IntegrityError

from logs.logger import Logger, CRITICAL, INFO

from helpers.exceptions import (
    InvalidCredentials,
    NullPassword,
    NullUsername,
    InvalidMemberName,
    MemberAlreadyExists,
    WeakPassword,
    UserRemovingSelf,
)
from utils.io_functions import show_message

import sys


def handle_exception(menu_func):

    def wrapper():
        try:
            result = menu_func()

        except ValueError:
            show_message("Invalid Choice.")

        except NullPassword:
            show_message("Password can't be empty.")

        except InvalidMemberName:
            show_message("Invalid username entered.")

        except MemberAlreadyExists:
            show_message("Member already is in team.")

        except NullUsername:
            show_message("Username can't be empty.")

        except WeakPassword:
            show_message("Your password is too weak.")
            show_message(
                "Password must be alteast 6 character long and must contain atleast 1 digit, 1 lowercase, 1 uppercase, 1 special character."
            )

        except InvalidCredentials:
            show_message("Invalid username or password.")

        except IntegrityError:
            show_message("Username already exists.")

        except NotImplementedError:
            show_message("Will soon be implemented, have some patience!")

        except UserRemovingSelf:
            show_message("Leader can't be removed from the team.")

        except SystemExit:
            Logger.log(INFO, "Closing System.")
            show_message("Bye.")
            sys.exit(0)

        except Exception as error:
            Logger.log(CRITICAL,
                       f"Closing System due to unexpected error.<{error}>")
            show_message("Unexpected Error Occurred! Turning System Down...")
            sys.exit(1)

        else:
            return result

    return wrapper
