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
        site_url TEXT,
        site_username TEXT,
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

    PERSONAL_PASSWORDS = """
    SELECT * FROM passwords
    WHERE creator_id = ? AND password_type = 0;
    """

    PERSONAL_PASSWORDS_FILTER = """
    SELECT * FROM passwords
    WHERE creator_id = ? and password_type = 0
    AND (site_url LIKE ? or site_username LIKE ? or notes LIKE ?);
    """

    TEAM_PASSWORDS = """
    SELECT * FROM team_members
    WHERE member_id = ?
    INNER JOIN team_passwords WHERE team_passwords.team_id = team_members.team_id
    INNER JOIN passwords WHERE passwords.id = team_passwords.password_id;
    """

    TEAM_PASSWORDS_FILTER = """
    SELECT * FROM team_members
    WHERE member_id = ?
    INNER JOIN team_passwords ON team_passwords.team_id = team_members.team_id
    INNER JOIN passwords ON passwords.id = team_passwords.password_id
    AND (passwords.site_url LIKE ? or passwords.site_username LIKE ? or passwords.notes LIKE ?);
    """

    ADD_NEW_PASSWORD = """
    INSERT INTO passwords(creator_id, site_url, site_username, password_type, encrypted_password, notes)
    VALUES(?, ?, ?, ?, ?, ?)
    """

    DELETE_PASSWORD = """
    DELETE FROM passwords
    WHERE id = ?;
    """

    DELETE_TEAM_PASSWORD = """
    DELETE FROM team_passwords
    WHERE password_id = ?;
    """