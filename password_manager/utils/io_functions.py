"""
All the Input-Output related methods are defined here.
"""

import pwinput

from models.password import Password, PasswordStrength
from utils.crypt import Crypt
from helpers.exceptions import NullPassword, NullUsername, WeakPassword


def credential_input(check_strength=False):
    username = input("    Enter username:").strip()

    if not username:
        raise NullUsername

    password = pwinput.pwinput("    Enter password:").strip()

    if not password:
        raise NullPassword

    if check_strength and Password.strength("", password) in [
            PasswordStrength.WEAK,
            PasswordStrength.VERY_WEAK,
    ]:
        raise WeakPassword

    return username, password.encode()


def create_password_input():
    print("    Enter all the details with respect to the site:")

    site_url = input("    Enter site url(optional):")
    username = input("    Enter username(optional):")
    password = pwinput.pwinput("    Enter password:")

    if not password:
        raise NullPassword

    notes = input("    Enter any keynote(optional):")

    return site_url, username, Crypt.encrypt(password), notes


def search_key_input():
    return input("    Enter keywords for search:")


def password_ids_input():
    return input(
        "    Enter password ids to see password(comma seprated values or A for all):"
    )


def show_passwords(passwords, hide_password=True):
    print()
    print()
    print(
        f"    {'Id':6}\t{'URL':20}\t{'username':20}\t{'Password':20}\t{'Notes':40}\t{'Strength':20}"
    )
    for index, password in enumerate(passwords, start=1):
        print(f"    {password.description(index, hide_password)}")

    print()


def show_teams(teams):
    print()
    print()
    print(f"    {'Id':6}\t{'Team Name':20}")

    for index, team in enumerate(teams, start=1):
        print(f"    {str(index):6}\t{team}")

    print()


def show_members(members):
    print()
    print()
    print(f"    {'Id':6}\t{'Member Name':20}")

    for index, member in enumerate(members, start=1):
        print(f"    {str(index):6}\t{member}")

    print()


def show_message(message: str):
    print(f"""
    {message}""")


def create_team_input():
    return input("    Enter Team Name:")


def team_member_username_input():
    return input("    Enter username of the member:")


def select_by_id(data, data_name):
    index = input(f"    Enter {data_name} id:")

    if not index.isdigit():
        raise ValueError

    index = int(index) - 1

    if index < 0 or index > len(data) - 1:
        raise ValueError

    return data[index]
