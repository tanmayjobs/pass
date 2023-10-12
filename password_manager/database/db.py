import os
import sqlite3

class Database:

    __DB_PATH = "database/storage/"
    __DB_FILE = __DB_PATH + "db.sql"

    @staticmethod
    def init() -> None:
        if not os.path.exists(Database.__DB_PATH):
            os.mkdir("database/storage/")
