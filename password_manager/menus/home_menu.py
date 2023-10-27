"""
This file contains the home menu.
From here user can go to personal or team passwords.
"""

from controllers.authorizer import Authorizer

import menus.user_required_menu as user_required_menu
import menus.personal_password_menu as personal_password_menu
import menus.team_password_menu as team_password_menu
import menus.authentication_menu as authentication_menu


class HomeMenu(user_required_menu.UserRequiredMenu):
    prompt = """
    Press:
    - '1' to personal passwords
    - '2' to team passwords
    - '3' to sign out

    Your choice:"""

    def handler(self, user_choice):
        if user_choice == 1:
            return personal_password_menu.PersonalPasswordsMenu(self.user)
        elif user_choice == 2:
            return team_password_menu.TeamPasswordsMenu(self.user)
        elif user_choice == 3:
            Authorizer.sign_out()
            return authentication_menu.AuthenticationMenu
        raise ValueError("Invalid Choice.")
