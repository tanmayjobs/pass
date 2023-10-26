from sqlite3 import IntegrityError

from logs.logger import Logger, CRITICAL, INFO

from utils.helpers.exceptions import InvalidCredentials, NullPassword, NullUsername, InvalidMemberName
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

        except NullUsername:
            show_message("Username can't be empty.")

        except InvalidCredentials:
            show_message("Invalid username or password.")

        except IntegrityError:
            show_message("Username already exists.")

        except NotImplementedError:
            show_message("Will soon be implemented, have some patience!")

        except SystemExit:
            Logger.log(INFO, "Closing System.")
            show_message("Bye.")
            sys.exit(0)

        # except Exception as error:
        #     Logger.log(CRITICAL,
        #                f"Closing System due to unexpected error.<{error}>")
        #     show_message("Unexpected Error Occurred! Turning System Down...")
        #     sys.exit(0)

        else:
            return result

    return wrapper
