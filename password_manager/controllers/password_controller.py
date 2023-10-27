"""
This file contains password controller.
All the methods for passwords are defined here.
These methods are general and can handle personal and team both type of passwords.
"""

from logs.logger import Logger, ERROR

from models.user import User
from models.team import Team
from models.password import Password, PasswordType

from utils.io_functions import (
    create_password_input,
    search_key_input,
    password_id_input,
    password_ids_input,
)


class PasswordController:

    @staticmethod
    def show_true_passwords(passwords: list[Password]):
        try:
            user_input = password_ids_input()
            if user_input == 'A':
                return passwords

            selected_passwords_id = list(
                map(lambda x: int(x) - 1, user_input.split(",")))
            selected_passwords = [
                passwords[selected_id] for selected_id in selected_passwords_id
            ]

        except (TypeError, IndexError) as error:
            Logger.log(ERROR, error)
            raise ValueError

        except:
            raise

        else:
            return selected_passwords

    @staticmethod
    def get_passwords(
        user: User,
        key: bool = False,
        password_type: PasswordType = PasswordType.PERSONAL_PASSWORD,
    ):
        try:
            search_key = search_key_input() if key else ""

            passwords = Password.get_passwords(user, search_key, password_type)

        except Exception as error:
            Logger.log(ERROR, error)
            raise
        else:
            return passwords

    @staticmethod
    def add_password(user: User, team: Team = None):
        try:
            site_url, site_username, password, notes = create_password_input()
            Password.add_password(user, site_url, site_username, password,
                                  notes, team)

        except Exception as error:
            Logger.log(ERROR, error)
            raise

        else:
            return

    @staticmethod
    def delete_password(user: User, passwords: list[Password]):
        try:
            selected_password = int(password_id_input()) - 1
            password = passwords[selected_password]

            Password.delete_password(password)

        except (TypeError, IndexError) as error:
            Logger.log(ERROR, error)
            raise ValueError

        except Exception as error:
            Logger.log(ERROR, error)
            raise

        else:
            return

    @staticmethod
    def update_password(user: User, passwords: list[Password]):
        try:
            selected_password = int(password_id_input()) - 1
            password = passwords[selected_password]
            site_url, site_username, encrypted_password, notes = create_password_input(
            )

            Password.update_password(password, site_url, site_username,
                                     encrypted_password, notes)

        except (TypeError, IndexError) as error:
            Logger.log(ERROR, error)
            raise ValueError

        except Exception as error:
            Logger.log(ERROR, error)
            raise

        else:
            return
