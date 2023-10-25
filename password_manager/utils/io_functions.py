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


def show_passwords(passwords):
    print()
    print()
    print(f"{'Id':6}\t{'URL':20}\t{'username':20}\t{'Password':8}\t{'Notes':20}")
    for password in passwords:
        print(password)
    print()


def show_message(message: str):
    print(
        f"""
    {message}"""
    )
