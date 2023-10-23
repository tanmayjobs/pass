from models.user import BaseUser

import os
import sqlite3


class SQLDatabase:
    __DB_PATH = "database/storage/"
    __DB_FILE = __DB_PATH + "db.sql"

    @staticmethod
    def init() -> None:
        if not os.path.exists(SQLDatabase.__DB_PATH):
            os.mkdir("database/storage/")

    def valid_user(user: BaseUser) -> bool:
        ...
