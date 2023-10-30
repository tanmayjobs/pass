"""
This file contains the Password Model.
Password Model is created for each password saved by any type of user.
Password Model is capable of accessing the Database to perform CRUD operation related to passwords.
"""

from database.db import SQLDatabase, SQLQueries

from models.user import User

from utils.crypt import Crypt
from utils.helpers.enums import PasswordType, PasswordStrength

import re


class Password:
    """
    Password model which contains the details of password.
    """

    def __init__(
        self,
        password_id: int,
        creator_id: str,
        password_type: PasswordType,
        site_url: str,
        username: str,
        encrypted_password: str,
        notes: str,
    ) -> None:
        self.password_id = password_id
        self.creator_id = creator_id
        self.password_type = password_type
        self.site_url = site_url
        self.username = username
        self.encrypted_password = encrypted_password
        self.notes = notes

    @staticmethod
    def from_database(password_data: tuple):
        return Password(*password_data)

    def description(self, index=1, hide_password: bool = True) -> str:
        return f"{str(index):6}\t{self.site_url:20}\t{self.username:20}\t{(Crypt.decrypt(self.encrypted_password) if not hide_password else '*' * 6):20}\t{self.notes:40}\t{self.strength().name:20}"

    @staticmethod
    def get_passwords(
        user: User,
        search_key: str = "",
        password_type: PasswordType = PasswordType.PERSONAL_PASSWORD,
    ):
        db = SQLDatabase()

        if password_type == PasswordType.PERSONAL_PASSWORD:
            query = (SQLQueries.PERSONAL_PASSWORDS_FILTER
                     if search_key else SQLQueries.PERSONAL_PASSWORDS)
        else:
            query = (SQLQueries.TEAM_PASSWORDS_FILTER
                     if search_key else SQLQueries.TEAM_PASSWORDS)

        params = (
            *[f"%{search_key}%" for _ in range(3) if search_key],
            user.user_id,
        )

        passwords = db.get(query, params)
        passwords = [
            Password.from_database(password) for password in passwords
        ]

        return passwords

    @staticmethod
    def add_password(
        user: User,
        site_url: str,
        site_username: str,
        password: str,
        notes: str,
        team=None,
    ):
        db = SQLDatabase()
        last_transaction = db.add(
            SQLQueries.ADD_PASSWORD,
            (
                user.user_id,
                site_url,
                site_username,
                0 if not team else 1,
                password,
                notes,
            ),
        )

        if team:
            db.add(
                SQLQueries.ADD_TEAM_PASSWORD_MAPPING,
                (last_transaction.last_id, team.team_id),
            )

    @staticmethod
    def delete_password(password):
        db = SQLDatabase()
        db.remove(SQLQueries.DELETE_PASSWORD, (password.password_id, ))

        if password.password_type == PasswordType.TEAM_PASSWORD:
            db.remove(SQLQueries.DELETE_TEAM_PASSWORD,
                      (password.password_id, ))

    @staticmethod
    def update_password(password, site_url, site_username, encrypted_password,
                        notes):
        db = SQLDatabase()
        db.update(
            SQLQueries.UPDATE_PASSWORD,
            (
                site_url,
                site_username,
                encrypted_password,
                notes,
                password.password_id,
            ),
        )

    def strength(self, decrypted_password=None) -> PasswordStrength:
        if not decrypted_password:
            decrypted_password = Crypt.decrypt(self.encrypted_password)

        if re.match(PasswordStrength.EXCELLENT.value, decrypted_password):
            return PasswordStrength.EXCELLENT
        elif re.match(PasswordStrength.GOOD.value, decrypted_password):
            return PasswordStrength.GOOD
        elif re.match(PasswordStrength.WEAK.value, decrypted_password):
            return PasswordStrength.WEAK
        else:
            return PasswordStrength.VERY_WEAK
