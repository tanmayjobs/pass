"""
This file defines the base database class and database cursor.
Database class is used to create DB.
Database cursor is accessed only by models to interact with database.
"""

from database.queries import SQLQueries

import os
import sqlite3

DB_PATH = "database/storage/"
DB_FILE = DB_PATH + "database.db"


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

class LastTransaction:
    def __init__(self, lastrowid, rowcount) -> None:
        self.last_id = lastrowid
        self.rows_changed = rowcount

    @staticmethod
    def from_cursor(cursor):
        return LastTransaction(
            lastrowid=cursor.lastrowid,
            rowcount=cursor.rowcount
        )

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

    def get(self, query, params):
        with SQLCursor() as cursor:
            data = cursor.execute(query, params).fetchall()
            return data

    def add(self, query, params):
        with SQLCursor() as cursor:
            cursor.execute(query, params)
            return LastTransaction.from_cursor(cursor)

    def remove(self, query, params):
        with SQLCursor() as cursor:
            cursor.execute(query, params)

    def update(self, query , params):
        with SQLCursor() as cursor:
            cursor.execute(query, params)
