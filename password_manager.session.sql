SELECT passwords.id, passwords.creator_id, passwords.password_type, passwords.site_url, passwords.site_username, passwords.encrypted_password, passwords.notes FROM team_members
INNER JOIN team_passwords ON team_passwords.team_id = team_members.team_id
INNER JOIN passwords ON team_passwords.password_id = passwords.id
WHERE team_members.member_id = 1

-- SELECT * FROM team_members


-- INSERT INTO teams VALUES(NULL, 2, "First")
-- SELECT * FROM teams
-- INSERT INTO team_members VALUES(NULL, 1, 2)
-- SELECT * FROM team_members
-- INSERT INTO passwords VALUES(NULL, 2, 1, "TEST", "TEST", "ASDASD", "ASDASD")
-- SELECT * FROM passwords
-- INSERT INTO team_passwords VALUES(NULL, 4, 1)
-- SELECT * FROM team_passwords

-- DELETE FROM team_members