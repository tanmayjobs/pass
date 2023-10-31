"""
This file contains the authentication menu.
Here user can sign in or sign up.
And can also exit from the system.
"""

import controllers.authorizer as Authorizer
from utils.io_functions import credential_input
from utils.io_functions import show_message


class AuthenticationMenu:
    prompt = """
    Press:
    - '1' to sign in
    - '2' to sign up
    - '3' to exit

    Your choice:"""

    @staticmethod
    def handler(user_choice):
        if user_choice == 1:
            username, password = credential_input()
            user = Authorizer.sign_in(username, password)
            return user

        elif user_choice == 2:
            username, password = credential_input(check_strength=True)
            user_role = 1
            Authorizer.sign_up(username, password, user_role)

            show_message("User created successfuly.")

        elif user_choice == 3:
            raise SystemExit

        else:
            raise ValueError("Invalid Choice.")


class AuthenticationMenu:
    prompt = """
    Press:
    - '1' to sign in
    - '2' to sign up as user
    - '3' to sign up as team manager
    - '4' to exit

    Your choice:"""

    @staticmethod
    def handler(user_choice):
        if user_choice == 1:
            username, password = credential_input()
            user = Authorizer.sign_in(username, password)
            return user

        elif user_choice == 2 or user_choice == 3:
            username, password = credential_input(check_strength=True)
            user_role = 0 if user_choice == 3 else 1
            Authorizer.sign_up(username, password, user_role)

            show_message("User created successfuly.")

        elif user_choice == 4:
            raise SystemExit

        else:
            raise ValueError("Invalid Choice.")
