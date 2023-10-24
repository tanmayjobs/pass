from models.user import User

from handlers.before_auth.authentication_handler import AuthenticationHandler
from handlers.after_auth.password_handler import PasswordHandler

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
            user = AuthenticationHandler.sign_in()
            return user

        elif user_choice == 2 or user_choice == 3:
            user_role = 0 if user_choice == 3 else 1

            user = AuthenticationHandler.sign_up(user_role)
            return user

        elif user_choice == 4:
            raise SystemExit

        raise ValueError("Invalid Choice.")


class MainMenu:
    prompt = """
    Press:
    - '1' to personal passwords
    - '2' to team passowrds
    - '3' to sign out

    Your choice:"""

    @staticmethod
    def handler(user_choice, user: User):
        if user_choice == 1:
            return PersonalPasswordsMenu
        elif user_choice == 2:
            return TeamPasswordsMenu
        elif user_choice == 3:
            AuthenticationHandler.sign_out()
            return AuthenticationMenu
        raise ValueError("Invalid Choice.")

class PersonalPasswordsMenu:
    prompt = """
    Press:
    - '1' to list passwords
    - '2' to search password
    - '3' to add new password
    - '4' to delete password
    - '5' to update password
    - '6' to go back

    Your choice:"""

    @staticmethod
    def handler(user_choice, user: User):

        if user_choice == 1:
            PasswordHandler.get_all_passwords(user)
        elif user_choice == 2:
            ...
        elif user_choice == 3:
            PasswordHandler.add_new_password(user)
        elif user_choice == 4:
            ...
        elif user_choice == 5:
            ...
        elif user_choice == 6:
            return MainMenu
        else:
            raise ValueError("Invalid Choice.")

        return PersonalPasswordsMenu



class TeamPasswordsMenu:
    prompt = """
    Press:
    - '1' to list passwords
    - '2' to search password
    - '3' to add new password
    - '4' to delete password
    - '5' to update password
    - '6' to go back

    Your choice:"""

    @staticmethod
    def handler(user_choice, user: User):
        if user_choice == 1:
            ...
        elif user_choice == 2:
            ...
        elif user_choice == 3:
            AuthenticationHandler.sign_out()
            return AuthenticationMenu
        raise ValueError("Invalid Choice.")

