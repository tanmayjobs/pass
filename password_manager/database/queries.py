class SQLQueries:
    CREATE_AUTHENTICATION_TABLE = """
    CREATE TABLE IF NOT EXISTS authentication(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        user_role INTEGER CHECK (user_role IN (0, 1)) DEFAULT 1,
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
    WHERE (site_url LIKE ? or site_username LIKE ? or notes LIKE ?)
    AND creator_id = ? AND password_type = 0;
    """

    TEAM_PASSWORDS = """
    SELECT passwords.id, passwords.creator_id, passwords.password_type, passwords.site_url, passwords.site_username, passwords.encrypted_password, passwords.notes
    FROM team_members
    INNER JOIN team_passwords ON team_passwords.team_id = team_members.team_id
    INNER JOIN passwords ON team_passwords.password_id = passwords.id
    WHERE team_members.member_id = ?;
    """

    TEAM_PASSWORDS_FILTER = """
    SELECT passwords.id, passwords.creator_id, passwords.password_type, passwords.site_url, passwords.site_username, passwords.encrypted_password, passwords.notes
    FROM team_members
    INNER JOIN team_passwords ON team_passwords.team_id = team_members.team_id
    INNER JOIN passwords ON team_passwords.password_id = passwords.id
    AND (passwords.site_url LIKE ? or passwords.site_username LIKE ? or passwords.notes LIKE ?)
    WHERE member_id = ?
    """

    ADD_PASSWORD = """
    INSERT INTO passwords(creator_id, site_url, site_username, password_type, encrypted_password, notes)
    VALUES(?, ?, ?, ?, ?, ?);
    """

    DELETE_PASSWORD = """
    DELETE FROM passwords
    WHERE id = ?;
    """

    DELETE_TEAM_PASSWORD = """
    DELETE FROM team_passwords
    WHERE password_id = ?;
    """

    UPDATE_PASSWORD = """
    UPDATE passwords
    SET (site_url, site_username, encrypted_password, notes) = (?, ?, ?, ?)
    WHERE id = ?;
    """

    ALL_TEAMS = """
    SELECT * FROM teams
    WHERE creator_id = ?;
    """

    ADD_TEAM = """
    INSERT INTO teams
    VALUES(NULL, ?, ?);
    """

    DELETE_ALL_TEAM_PASSWORDS = """
    DELETE FROM passwords
    WHERE passwords.id IN(
        SELECT * FROM passwords
        INNER JOIN team_passwords ON team_passwords.password_id = passwords.id AND team_passwords.team_id = ?
        WHERE password_type = 1
    ) AND passwords.creator_id = ?;
    """

    DELETE_ALL_TEAM_MEMBERS = """
    DELETE FROM team_members
    WHERE team_id = ?;
    """

    DELETE_ALL_TEAM_PASSWORDS_RECORDS = """
    DELETE FROM team_passwords
    WHERE id team_id = ?;
    """

    DELETE_TEAM = """
    DELETE FROM teams
    WHERE id = ?;
    """
