"""
This file contains team controller.
All the methods related to team are defined here.
"""

from logs.logger import Logger, ERROR

from helpers.exceptions import InvalidMemberName, MemberAlreadyExists, UserRemovingSelf

from models.user import User
from models.team import Team

from sqlite3 import IntegrityError

from utils.io_functions import (create_team_input, team_member_username_input,
                                show_members, select_by_id)




def get_teams(user: User):
    try:
        teams = Team.get_teams(user)
    except:
        raise
    else:
        return teams


def add_team(user: User, team_name: str):
    try:
        Team.add(user, team_name)
    except:
        raise
    else:
        return


def delete_team(team: Team, user: User):
    try:
        Team.delete(user, team)
    except (TypeError, IndexError) as error:
        Logger.log(ERROR, error)
        raise ValueError
    except:
        raise
    else:
        return


def add_member(user: User, team: Team, member_name):
    all_members = team.members()

    for member in all_members:
        if member.username == member_name:
            raise MemberAlreadyExists

    if member_name == user.username:
        raise InvalidMemberName
    try:
        team.add_member(team, member_name)
    except IntegrityError:
        raise InvalidMemberName
    except:
        raise
    else:
        return


def delete_member(user: User, team: Team, member_id):
    try:

        if member_id == user.user_id:
            raise UserRemovingSelf

        team.delete_member(member_id)
    except (TypeError, IndexError) as error:
        Logger.log(ERROR, error)
        raise ValueError
    except:
        raise
    else:
        return
