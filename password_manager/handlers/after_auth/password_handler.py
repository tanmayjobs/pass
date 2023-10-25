from database.db import SQLCursor
from database.queries import SQLQueries

from models.user import User, UserType
from models.password import Password, PasswordType

from utils.io_functions import (
    create_password_input,
    search_key_input,
    password_id_input,
)


class PasswordHandler:
    @staticmethod
    def get_passwords(user: User, key: bool = False):
        if key:
            search_key = search_key_input()
        try:
            with SQLCursor() as cursor:
                query = (
                    SQLQueries.PERSONAL_PASSWORDS_FILTER
                    if key
                    else SQLQueries.PERSONAL_PASSWORDS
                )
                params = (user.user_id, *[f'%{search_key}%' for _ in range(3) if key])

                passwords = cursor.execute(query, params).fetchall()
                passwords = [Password.from_database(password) for password in passwords]

        except:
            raise
        else:
            return passwords

    @staticmethod
    def add_new_password(user: User):
        site_url, site_username, password, notes = create_password_input()
        try:
            with SQLCursor() as cursor:
                cursor.execute(
                    SQLQueries.ADD_NEW_PASSWORD,
                    (user.user_id, site_url, site_username, 0, password, notes),
                )

        except:
            raise

        else:
            return

    @staticmethod
    def delete_password(user: User):
        password_id = password_id_input()
        try:
            with SQLCursor() as cursor:
                cursor.execute(SQLQueries.DELETE_PASSWORD, (password_id,))
                cursor.execute(SQLQueries.DELETE_TEAM_PASSWORD, (password_id,))

        except:
            raise

        else:
            return

    @staticmethod
    def update_password(user: User):
        password_id = password_id_input()
        site_url, site_username, password, notes = create_password_input()

        try:
            with SQLCursor() as cursor:
                cursor.execute(
                    SQLQueries.UPDATE_PASSWORD,
                    (site_url, site_username, password, notes, password_id),
                )

        except:
            raise

        else:
            return