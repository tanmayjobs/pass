from database.db import SQLCursor
from database.queries import SQLQueries

from models.user import User, UserType
from models.password import Password, PasswordType

from utils.io_functions import create_password_input


class PasswordHandler:

    @staticmethod
    def get_all_passwords(user):
        try:
            with SQLCursor() as cursor:
                all_passwords = cursor.execute(
                    SQLQueries.PERSONAL_PASSWORDS, (user.user_id,)
                ).fetchall()

        except:
            # logging for invalid attempt
            raise
        else:
            return all_passwords

    @staticmethod
    def add_new_password(user):
        site_url, site_username, password, notes = create_password_input()
        try:
            with SQLCursor() as cursor:
                cursor.execute(
                    SQLQueries.ADD_NEW_PASSWORD, (user.user_id,site_url, site_username, 0, password, notes)
                )

        except:
            # logging for invalid attempt
            raise
        else:
            return
