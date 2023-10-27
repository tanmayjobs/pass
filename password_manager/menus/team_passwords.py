"""
This file contains Team Password Menu.
Here user can view there team passwords.
And Team Managers have extra feature of Team Management.
"""

from controllers.password import PasswordController

from models.user import UserType
from models.password import PasswordType

from utils.io_functions import show_passwords, show_message

import menus.teams_management as teams_management
import menus.user_required_menu as user_required_menu
import menus.home_menu as home_menu


class TeamPasswordsMenu(user_required_menu.UserRequiredMenu):
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
            passwords = PasswordController.get_passwords(
                self.user, user_choice == 2, PasswordType.TEAM_PASSWORD)
            if not passwords:
                show_message(f"You haven't saved any password yet.")
            else:
                show_passwords(passwords)
                passwords = PasswordController.show_true_passwords(passwords)
                show_passwords(passwords, False)

        elif user_choice == 3:
            return home_menu.HomeMenu(self.user)

        else:
            raise ValueError("Invalid Choice.")

        return self

    def team_manager_handler(self, user_choice):
        if user_choice == 1 or user_choice == 2:
            passwords = PasswordController.get_passwords(
                self.user, user_choice == 2, PasswordType.TEAM_PASSWORD)
            if not passwords:
                show_message(f"You haven't saved any password yet.")
            else:
                show_passwords(passwords)
                passwords = PasswordController.show_true_passwords(passwords)
                show_passwords(passwords, False)

        elif user_choice == 3:
            return teams_management.TeamsManagementMenu(self.user)

        elif user_choice == 4:
            return home_menu.HomeMenu(self.user)

        else:
            raise ValueError("Invalid Choice.")

        return self

    def handler(self, user_choice):
        if self.user.user_type == UserType.BASIC_USER:
            return self.user_handler(user_choice)

        return self.team_manager_handler(user_choice)
