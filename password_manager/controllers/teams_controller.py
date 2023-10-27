from logs.logger import Logger, ERROR

from utils.helpers.exceptions import InvalidMemberName, MemberAlreadyExists

from models.user import User
from models.team import Team

from sqlite3 import IntegrityError

from utils.io_functions import (
    create_team_input,
    team_id_input,
    team_member_username_input,
    member_id_input,
    show_members,
    show_message,
)


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
            Team.delete(user, team)
        except (TypeError, IndexError) as error:
            Logger.log(ERROR, error)
            raise ValueError
        except:
            raise
        else:
            return

    @staticmethod
    def choose_team(teams: list[Team]):
        try:
            selected_team = int(team_id_input()) - 1
            team = teams[selected_team]
        except (TypeError, IndexError) as error:
            Logger.log(ERROR, error)
            raise ValueError
        except:
            raise
        else:
            return team

    @staticmethod
    def add_member(user: User, team: Team):
        all_members = team.members()
        member_username = team_member_username_input()

        for member in all_members:
            if member.username == member_username:
                raise MemberAlreadyExists

        if member_username == user.username:
            raise InvalidMemberName
        try:
            team.add_member(team, member_username)
        except IntegrityError:
            raise InvalidMemberName
        except:
            raise
        else:
            return

    @staticmethod
    def delete_member(team: Team):
        try:
            all_members = team.members()

            if not all_members:
                show_message("There are no members in your team, except you.")
            else:
                show_members(all_members)

                member_id = int(member_id_input()) - 1
                team.delete_member(member_id)
        except (TypeError, IndexError) as error:
            Logger.log(ERROR, error)
            raise ValueError
        except:
            raise
        else:
            return
