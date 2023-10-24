import getpass

def credential_input():
    username = input("""    Enter username:""")
    password = getpass.getpass("""    Enter password:""")

    return username, password.encode('utf-8')