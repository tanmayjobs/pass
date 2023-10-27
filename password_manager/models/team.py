"""
This file contains the Team Model.
Team Model is created for each team created by team manager.
Team Model is capable of accessing the Database to perform CRUD operation related to teams.
"""

from database.db import SQLCursor, SQLQueries

from utils.helpers.exceptions import InvalidMemberName

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

    @staticmethod
    def get_teams(user: User):
        with SQLCursor() as cursor:
            teams = cursor.execute(SQLQueries.ALL_TEAMS,
                                   (user.user_id, )).fetchall()
            teams = [Team.from_database(team) for team in teams]

        return teams

    @staticmethod
    def add(user: User, team_name: str):
        with SQLCursor() as cursor:
            cursor.execute(SQLQueries.ADD_TEAM, (user.user_id, team_name))
            cursor.execute(SQLQueries.ADD_TEAM_LEADER,
                           (cursor.lastrowid, user.user_id))

    @staticmethod
    def delete(user: User, team):
        with SQLCursor() as cursor:
            cursor.execute(SQLQueries.DELETE_ALL_TEAM_PASSWORDS,
                           (team.team_id, user.user_id))
            cursor.execute(SQLQueries.DELETE_ALL_TEAM_MEMBERS,
                           (team.team_id, ))
            cursor.execute(SQLQueries.DELETE_ALL_TEAM_PASSWORDS_RECORDS,
                           (team.team_id, ))
            cursor.execute(SQLQueries.DELETE_TEAM, (team.team_id, ))

    @staticmethod
    def add_member(team, member_username: str):
        with SQLCursor() as cursor:
            cursor.execute(SQLQueries.ADD_MEMBER,
                           (team.team_id, member_username))
            if not cursor.rowcount:
                raise InvalidMemberName

    def delete_member(self, member_id: str):
        with SQLCursor() as cursor:
            cursor.execute(SQLQueries.DELETE_MEMBER, (self.team_id, member_id))

    def members(self):
        with SQLCursor() as cursor:
            all_members = cursor.execute(SQLQueries.GET_MEMBERS,
                                         (self.team_id, )).fetchall()
            return [User.from_database(member) for member in all_members]
