from database.queries import SQLQueries

import os
import sqlite3

DB_PATH = "database/storage/"
DB_FILE = DB_PATH + "db.sql"


class SQLCursor:
    def __enter__(self):
        global DB_FILE, DB_PATH
        self.connection = sqlite3.connect(DB_FILE)
        self.cursor = self.connection.cursor()

        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        global DB_FILE, DB_PATH
        self.connection.commit()
        self.connection.close()


class SQLDatabase:
    @staticmethod
    def initialize() -> None:
        global DB_FILE, DB_PATH
        if not os.path.exists(DB_PATH):
            os.mkdir("database/storage/")

        with SQLCursor() as cursor:
            cursor.execute(SQLQueries.CREATE_AUTHENTICATION_TABLE)
            cursor.execute(SQLQueries.CREATE_PASSWORDS_TABLE)
            cursor.execute(SQLQueries.CREATE_TEAMS_TABLE)
            cursor.execute(SQLQueries.CREATE_TEAM_PASSWORDS_TABLE)
            cursor.execute(SQLQueries.CREATE_TEAM_MEMBERS_TABLE)
