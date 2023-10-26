from database.db import SQLCursor, SQLQueries
from logs.logger import Logger, DEBUG, logging

from models.user import User


class Team:
    """
    Team model which contains all the team's details,
    including all the passwords, creator and members of team.
    """

    def __init__(self, team_id: str, creator_id: str, team_name: str) -> None:
        self.team_id = team_id
        self.creator_id = creator_id
        self.team_name = team_name

    @staticmethod
    def from_database(team_data: tuple) -> "Team":
        return Team(*team_data)

    def __repr__(self) -> str:
        return f"{self.team_name:20}"

    def get_teams(user: User):
        with SQLCursor() as cursor:
            teams = cursor.execute(SQLQueries.ALL_TEAMS,
                                   (user.user_id, )).fetchall()
            teams = [Team.from_database(team) for team in teams]

        return teams

    def add(user: User, team_name: str):
        with SQLCursor() as cursor:
            cursor.execute(SQLQueries.ADD_TEAM, (user.user_id, team_name))

    def remove(user: User, team):
        with SQLCursor() as cursor:
            cursor.execute(SQLQueries.DELETE_ALL_TEAM_PASSWORDS,
                           (team.team_id, user.user_id))
            cursor.execute(SQLQueries.DELETE_ALL_TEAM_MEMBERS,
                           (team.team_id, ))
            cursor.execute(SQLQueries.DELETE_ALL_TEAM_PASSWORDS_RECORDS,
                           (team.team_id, ))
            cursor.execute(SQLQueries.DELETE_TEAM, (team.team_id, ))

    def add_member(user: User, team, member_name: str):
        ...
