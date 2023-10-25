from models.user import UserType

from handlers.before_auth.authentication_handler import AuthenticationHandler
from handlers.after_auth.password_handler import PasswordHandler
from handlers.after_auth.team_password_handler import TeamPasswordHandler

from utils.io_functions import show_passwords, show_message


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


class UserHandlingMenu:
    def __init__(self, user) -> None:
        self.user = user


class MainMenu(UserHandlingMenu):
    prompt = """
    Press:
    - '1' to personal passwords
    - '2' to team passowrds
    - '3' to sign out

    Your choice:"""

    def handler(self, user_choice):
        if user_choice == 1:
            return PersonalPasswordsMenu(self.user)
        elif user_choice == 2:
            return TeamPasswordsMenu(self.user)
        elif user_choice == 3:
            AuthenticationHandler.sign_out()
            return AuthenticationMenu
        raise ValueError("Invalid Choice.")


class PersonalPasswordsMenu(UserHandlingMenu):
    prompt = """
    Press:
    - '1' to list passwords
    - '2' to search password
    - '3' to add new password
    - '4' to delete password
    - '5' to update password
    - '6' to go back

    Your choice:"""

    def handler(self, user_choice):
        if user_choice == 1 or user_choice == 2 or user_choice == 4 or user_choice == 5:
            passwords = PasswordHandler.get_passwords(self.user, user_choice == 2)

            if not passwords:
                show_message(f"Nothing to {'delete' if user_choice == 4 else 'show'}.")
            else:
                show_passwords(passwords)
                if user_choice == 4:
                    PasswordHandler.delete_password(passwords, self.user)
                elif user_choice == 5:
                    PasswordHandler.update_password(passwords, self.user)

        elif user_choice == 3:
            PasswordHandler.add_new_password(self.user)

        elif user_choice == 5:
            raise NotImplementedError

        elif user_choice == 6:
            return MainMenu(self.user)

        else:
            raise ValueError("Invalid Choice.")

        return self


class TeamPasswordsMenu(UserHandlingMenu):
    user_prompt = """
    Press:
    - '1' to list passwords
    - '2' to search password
    - '3' to go back

    Your choice:"""

    team_manager_prompt = """
    Press:
    - '1' to list passwords
    - '2' to search password
    - '3' to manage team
    - '4' to go back

    Your choice:"""

    @property
    def prompt(self):
        if self.user.user_type == UserType.BASIC_USER:
            return TeamPasswordsMenu.user_prompt

        return TeamPasswordsMenu.team_manager_prompt

    def user_handler(self, user_choice):
        if user_choice == 1 or user_choice == 2:
            passwords = TeamPasswordHandler.get_passwords(self.user, user_choice == 2)
            show_passwords(passwords)

        elif user_choice == 3:
            return MainMenu(self.user)

        else:
            raise ValueError("Invalid Choice.")

        return self

    def team_manager_handler(self, user_choice):
        if user_choice == 1 or user_choice == 2:
            passwords = TeamPasswordHandler.get_passwords(self.user, user_choice == 2)
            show_passwords(passwords)

        elif user_choice == 3:
            raise NotImplementedError

        elif user_choice == 4:
            return MainMenu(self.user)

        else:
            raise ValueError("Invalid Choice.")

        return self

    def handler(self, user_choice):
        if self.user.user_type == UserType.BASIC_USER:
            return self.user_handler(user_choice)

        return self.team_manager_handler(user_choice)
