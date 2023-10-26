from database.db import SQLCursor
from database.queries import SQLQueries

from models.user import User
from models.team import Team

from utils.io_functions import create_team_input, team_id_input


class TeamsController:

    @staticmethod
    def get_teams(user: User):
        try:
            teams = Team.get_teams(user)
        except:
            raise
        else:
            return teams

    @staticmethod
    def add_team(user: User):
        try:
            team_name = create_team_input()
            Team.add(user, team_name)
        except:
            raise
        else:
            return

    @staticmethod
    def delete_team(teams: list[Team], user: User):
        try:
            selected_team = int(team_id_input()) - 1
            team = teams[selected_team]
            Team.remove(user, team)
        except:
            raise
        else:
            return

    @staticmethod
    def choose_team(teams: list[Team]):
        try:
            selected_team = int(team_id_input()) - 1
            team = teams[selected_team]
        except:
            raise
        else:
            return team
