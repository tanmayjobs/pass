import getpass


def credential_input():
    username = input("    Enter username:")
    password = getpass.getpass("    Enter password:")

    return username, password.encode("utf-8")


def create_password_input():
    print("    Enter all the details with respect to the site:")

    site_url = input("    Enter site url(optional):")
    username = input("    Enter username(optional):")
    password = getpass.getpass("    Enter password:")
    notes = input("    Enter any keynote(optional):")

    return site_url, username, password.encode("utf-8"), notes


def search_key_input():
    return input("    Enter keywords for search:")


def password_id_input():
    return input("    Enter password id:")


def password_ids_input():
    return input("    Enter password ids(comma seprated values or A for all):")


def show_passwords(passwords, hide_password=True):
    print()
    print()
    print(f"    {'Id':6}\t{'URL':20}\t{'username':20}\t{'Password':20}\t{'Notes':20}")
    for index, password in enumerate(passwords, start=1):
        print(f'    {password.description(index, hide_password)}')

    print()


def show_teams(teams):
    print()
    print()
    print(f"    {'Id':6}\t{'Team Name':20}")

    for index, team in enumerate(teams, start=1):
        print(f"    {index:6}\t{team}")

    print()


def show_message(message: str):
    print(
        f"""
    {message}"""
    )


def create_team_input():
    return input("    Enter Team Name:")


def team_id_input():
    return input("    Enter team id:")
