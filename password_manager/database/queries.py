class SQLQueries:
    CREATE_AUTHENTICATION_TABLE = """
    CREATE TABLE IF NOT EXISTS authentication(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        user_role INTEGER CHECK (user_role IN (0, 1)) DEFAULT 0,
        is_deleted BOOL NOT NULL DEFAULT False,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    """

    CREATE_PASSWORDS_TABLE = """
    CREATE TABLE IF NOT EXISTS passwords(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        creator_id INTEGER,
        password_type INTEGER CHECK (password_type IN (0, 1)),
        username TEXT,
        encrypted_password TEXT NOT NULL,
        notes TEXT,
        FOREIGN KEY(creator_id) REFERENCES authentication(id)
    );
    """

    CREATE_TEAMS_TABLE = """
    CREATE TABLE IF NOT EXISTS teams(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        creator_id INTEGER NOT NULL,
        teamname TEXT NOT NULL,
        FOREIGN KEY(creator_id) REFERENCES authentication(id)
    );
    """

    CREATE_TEAM_PASSWORDS_TABLE = """
    CREATE TABLE IF NOT EXISTS team_passwords(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        FOREIGN KEY(password_id) REFERENCES passwords(id),
        FOREIGN KEY(team_id) REFERENCES teams(id)
    );
    """

    CREATE_TEAM_MEMBERS_TABLE = """
    CREATE TABLE IF NOT EXISTS team_members(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_id INTEGER NOT NULL,
        member_id INTEGER NOT NULL,
        FOREIGN KEY(team_id) REFERENCES teams(id),
        FOREIGN KEY(member_id) REFERENCES authentication(id)
    );
    """

    SIGN_IN = """
    SELECT * FROM authentication
    WHERE username = ?;
    """

    SIGN_UP = """
    INSERT INTO authentication(username, password_hash, user_role)
    VALUES(?, ?, ?);
    """