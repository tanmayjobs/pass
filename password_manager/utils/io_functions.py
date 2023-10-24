import getpass

def credential_input():
    username = input("    Enter username:")
    password = getpass.getpass("    Enter password:")

    return username, password.encode('utf-8')

def create_password_input():
    print("    Enter all the details with respect to the site:")

    site_url = input("    Enter site url(optional):")
    username = input("    Enter username(optional):")
    password =  getpass.getpass("    Enter password:")
    notes = input("    Enter any keynote(optional):")

    return site_url, username, password.encode('utf-8'), notes