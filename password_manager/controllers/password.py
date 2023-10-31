"""
This file contains password controller.
All the methods for passwords are defined here.
These methods are general and can handle personal and team both type of passwords.
"""

from logs.logger import Logger, ERROR

from models.user import User
from models.team import Team
from models.password import Password, PasswordType


def show_true_passwords(passwords: list[Password], user_input):
    try:
        if user_input == "A":
            return passwords

        selected_passwords_id = list(map(lambda x: int(x) - 1, user_input.split(",")))
        selected_passwords = [
            passwords[selected_id] for selected_id in selected_passwords_id
        ]

    except (TypeError, IndexError) as error:
        Logger.log(ERROR, error)
        raise ValueError

    except:
        raise

    else:
        return selected_passwords


def get_passwords(
    user: User,
    team: Team = None,
    search_key: str = '',
    password_type: PasswordType = PasswordType.PERSONAL_PASSWORD,
):
    try:
        passwords = Password.get_passwords(user, team, search_key, password_type)

    except Exception as error:
        Logger.log(ERROR, error)
        raise
    else:
        return passwords


def add_password(user: User, site_url, site_username, password, notes, team: Team = None):
    try:
        Password.add_password(
            user,
            site_url,
            site_username,
            password,
            notes,
            team,
        )

    except Exception as error:
        Logger.log(ERROR, error)
        raise

    else:
        return


def delete_password(password):
    try:
        Password.delete_password(password)

    except (TypeError, IndexError) as error:
        Logger.log(ERROR, error)
        raise ValueError

    except Exception as error:
        Logger.log(ERROR, error)
        raise

    else:
        return


def update_password(password, site_url, site_username, encrypted_password, notes):
    try:
        Password.update_password(
            password, site_url, site_username, encrypted_password, notes
        )

    except (TypeError, IndexError) as error:
        Logger.log(ERROR, error)
        raise ValueError

    except Exception as error:
        Logger.log(ERROR, error)
        raise

    else:
        return
