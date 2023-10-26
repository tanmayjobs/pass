from models.user import UserType
from models.password import PasswordType

from handlers.before_auth.authentication_handler import AuthenticationHandler
from handlers.after_auth.password_handler import PasswordHandler

from handlers.after_auth.teams_handler import TeamsHandler

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


class UserRequired:
    def __init__(self, user) -> None:
        self.user = user


class TeamRequired:
    def __init__(self, team) -> None:
        self.team = team


class MainMenu(UserRequired):
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


class PersonalPasswordsMenu(UserRequired):
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
                show_message(f"You haven't saved any password yet.")
            else:
                show_passwords(passwords)
                if user_choice < 3:
                    passwords = PasswordHandler.show_true_passwords(passwords)
                    show_passwords(passwords, False)
                if user_choice == 4:
                    PasswordHandler.delete_password(self.user, passwords)
                    show_message("Password deleted successfuly.")
                elif user_choice == 5:
                    PasswordHandler.update_password(self.user, passwords)
                    show_message("Password updated successfuly.")

        elif user_choice == 3:
            PasswordHandler.add_password(self.user)
            show_message("Password added successfuly.")

        elif user_choice == 6:
            return MainMenu(self.user)

        else:
            raise ValueError("Invalid Choice.")

        return self


class TeamPasswordsMenu(UserRequired):
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
    - '3' to manage your teams
    - '4' to go back

    Your choice:"""

    @property
    def prompt(self):
        if self.user.user_type == UserType.BASIC_USER:
            return TeamPasswordsMenu.user_prompt

        return TeamPasswordsMenu.team_manager_prompt

    def user_handler(self, user_choice):
        if user_choice == 1 or user_choice == 2:
            passwords = PasswordHandler.get_passwords(self.user, user_choice == 2, PasswordType.TEAM_PASSWORD)
            if not passwords:
                show_message(f"You haven't saved any password yet.")
            else:
                show_passwords(passwords)
                passwords = PasswordHandler.show_true_passwords(passwords)
                show_passwords(passwords, False)

        elif user_choice == 3:
            return MainMenu(self.user)

        else:
            raise ValueError("Invalid Choice.")

        return self

    def team_manager_handler(self, user_choice):
        if user_choice == 1 or user_choice == 2:
            passwords = PasswordHandler.get_passwords(self.user, user_choice == 2, PasswordType.TEAM_PASSWORD)
            show_passwords(passwords)
            if not passwords:
                show_message(f"You haven't saved any password yet.")
            else:
                show_passwords(passwords)
                passwords = PasswordHandler.show_true_passwords(passwords)
                show_passwords(passwords, False)

        elif user_choice == 3:
            return TeamsManagementMenu(self.user)

        elif user_choice == 4:
            return MainMenu(self.user)

        else:
            raise ValueError("Invalid Choice.")

        return self

    def handler(self, user_choice):
        if self.user.user_type == UserType.BASIC_USER:
            return self.user_handler(user_choice)

        return self.team_manager_handler(user_choice)


class TeamsManagementMenu(UserRequired):
    prompt = """
    Press:
    - '1' to add team
    - '2' to delete team
    - '3' to manage team
    - '4' to go back

    Your choice:"""

    def handler(self, user_choice):
        if user_choice == 1:
            TeamsHandler.add_team(self.user)
        elif user_choice == 2:
            TeamsHandler.delete_team(teams, self.user)
        elif user_choice == 3:
            raise NotImplementedError
        elif user_choice == 4:
            return TeamPasswordsMenu(self.user)
        else:
            raise ValueError("Invalid Choice.")

        return self


class TeamManagementMenu(UserRequired):
    prompt = """
    Press:
    - '1' to add team member
    - '2' to remove team member
    - '3' to add password
    - '4' to delete password
    - '5' to update password
    - '4' to go back

    Your choice:"""

    def handler(self, user_choice):
        ...
