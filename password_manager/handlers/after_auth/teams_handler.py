from database.db import SQLCursor
from database.queries import SQLQueries

from models.user import User
from models.team import Team

from utils.io_functions import create_team_input, team_id_input


class TeamsHandler:
    @staticmethod
    def get_teams(user: User):
        try:
            with SQLCursor() as cursor:
                teams = cursor.execute(SQLQueries.ALL_TEAMS, (user.user_id,)).fetchall()
                teams = [Team.from_database(team) for team in teams]
        except:
            raise
        else:
            return teams

    @staticmethod
    def add_team(user: User):
        try:
            team_name = create_team_input()
            with SQLCursor() as cursor:
                cursor.execute(SQLQueries.ADD_TEAM, (user.user_id, team_name))
        except:
            raise
        else:
            return

    @staticmethod
    def delete_team(teams: list[Team], user: User):
        try:
            selected_team = int(team_id_input()) - 1
            team_id = teams[selected_team].team_id
            with SQLCursor() as cursor:
                cursor.execute(SQLQueries.DELETE_ALL_TEAM_PASSWORDS, (team_id, user.user_id))
                cursor.execute(SQLQueries.DELETE_ALL_TEAM_MEMBERS, (team_id,))
                cursor.execute(SQLQueries.DELETE_ALL_TEAM_PASSWORDS_RECORDS, (team_id,))
                cursor.execute(SQLQueries.DELETE_TEAM, (team_id))
        except:
            raise
        else:
            return
