from database.db import SQLCursor, SQLQueries

from models.user import User

from utils.crypt import Crypt
from utils.helpers.enums import PasswordType, PasswordStrength


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
        return f"{str(index):6}\t{self.site_url:20}\t{self.username:20}\t{(Crypt.decrypt(self.encrypted_password) if not hide_password else '*' * 6):20}\t{self.notes:20}\t{self.strength().name:20}"

    @staticmethod
    def get_passwords(
        user: User,
        search_key: str = "",
        password_type: PasswordType = PasswordType.PERSONAL_PASSWORD,
    ):
        with SQLCursor() as cursor:
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

            passwords = cursor.execute(query, params).fetchall()
            passwords = [
                Password.from_database(password) for password in passwords
            ]

        return passwords

    @staticmethod
    def add_password(user: User,
                     site_url: str,
                     site_username: str,
                     password: str,
                     notes: str,
                     team=None):
        with SQLCursor() as cursor:
            cursor.execute(
                SQLQueries.ADD_PASSWORD,
                (user.user_id, site_url, site_username, 0 if not team else 1,
                 password, notes),
            )

            if team:
                cursor.execute(SQLQueries.ADD_TEAM_PASSWORD_MAPPING,
                               (cursor.lastrowid, team.team_id))

    @staticmethod
    def delete_password(password):
        with SQLCursor() as cursor:
            cursor.execute(SQLQueries.DELETE_PASSWORD,
                           (password.password_id, ))
            if password.password_type == PasswordType.TEAM_PASSWORD:
                cursor.execute(SQLQueries.DELETE_TEAM_PASSWORD,
                               (password.password_id, ))

    @staticmethod
    def update_password(password, site_url, site_username, encrypted_password,
                        notes):
        with SQLCursor() as cursor:
            cursor.execute(
                SQLQueries.UPDATE_PASSWORD,
                (site_url, site_username, encrypted_password, notes,
                 password.password_id),
            )

    def strength(self) -> PasswordStrength:
        decrypted_password = Crypt.decrypt(self.encrypted_password)

        if len(decrypted_password) >= 10:
            return PasswordStrength.EXCELLENT
        elif len(decrypted_password) >= 8:
            return PasswordStrength.GOOD
        elif len(decrypted_password) >= 6:
            return PasswordStrength.WEAK
        else:
            return PasswordStrength.NONE
