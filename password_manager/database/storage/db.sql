SQLite format 3   @                                                                     .j�� 	= G��~�
i	=                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   �)%%�tableteam_membersteam_membersCREATE TABLE team_members(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_id INTEGER NOT NULL,
        member_id INTEGER NOT NULL,
        FOREIGN KEY(team_id) REFERENCES teams(id),
        FOREIGN KEY(member_id) REFERENCES authentication(id)
    )�.))�tableteam_passwordsteam_passwordsCREATE TABLE team_passwords(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        FOREIGN KEY(password_id) REFERENCES passwords(id),
        FOREIGN KEY(team_id) REFERENCES teams(id)
    )�a�!tableteamsteamsCREATE TABLE teams(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        creator_id INTEGER NOT NULL,
        teamname TEXT NOT NULL,
        FOREIGN KEY(creator_id) REFERENCES authentication(id)
    )�t�7tablepasswordspasswordsCREATE TABLE passwords(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        creator_id INTEGER,
        password_type INTEGER CHECK (password_type IN (0, 1)),
        site_url TEXT,
        site_username TEXT,
        encrypted_password TEXT NOT NULL,
        notes TEXT,
        FOREIGN KEY(creator_id) REFERENCES authentication(id)
    )P++Ytablesqlite_sequencesqlite_sequenceCREATE TABLE sqlite_sequence(name,seq)�q))�tableauthenticationauthenticationCREATE TABLE authentication(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        user_role INTEGER CHECK (user_role IN (0, 1)) DEFAULT 1,
        is_deleted BOOL NOT NULL DEFAULT False,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );O) indexsqlite_autoindex_authentication_1authentication          C �C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       \ �3Admin$2b$12$BRbwjrP2VS0qtALxCcKFVuhey5VM5dU53IclgVDxs7ZUb/YHCqzWe2023-10-26 11:14:44] �	3Tanmay$2b$12$Cpt8xrswKXdIf66gycs27.A.gs/w/9KVxw.DanxpKt3Pllaa1Odm.2023-10-26 11:12:15
   � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                	Admin		Tanmay� � ���                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            )authenticationpasswords   	aut	teams   g w�g�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        m	 	�TgAAAAABlOk2b7JrqgohTTlXX78crFjLOYYCqm8Fv9hGOkoCfRE3OcEibQqdHfCD3ocwthEpNF_r86dt957O9ID8nJKdxT9jf0Q==�		 	!�T%reddit.comtanmaygAAAAABlOknRmokkvhXn6Oww1ppzU1TSlstOJEUlN5lnbfF3MVsvXjXytShPe-y4mFhaMnQD8dxkjbUZZ8wMt_HIeKU5HTqLoQ==fun & office�	 	�TfirefoxfiregAAAAABlOknBCWgwbgD98gOpwZSK_r2w2h-_t1W4UhU8r2GiqI5p4FPQIXTyCN_tgyI0kfE_z3aSQOVqAnBlkQ9JAYJhhKO2Vg==home only�	 	�T!gmail.comtanmaygAAAAABlOkm18HLaUthyW1XYDLD_3MAU-r6Y2pLUfQYJdla3Ekg6lgmcvpmfIDAb1g2dgOUXMv-asD6mXZB4eBuSG5ZFmTyP-g==home & fun   � ��                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            Firebase AWS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            