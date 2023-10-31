"""
This file contains the home menu.
From here user can go to personal or team passwords.
"""

import controllers.authorizer as Authorizer

import menus.user_required_menu as user_required_menu
import menus.personal_passwords as personal_passwords
import menus.team_passwords as team_passwords
import menus.authentication as authentication


class HomeMenu(user_required_menu.UserRequiredMenu):
    prompt = """
    Press:
    - '1' to personal passwords
    - '2' to team passwords
    - '3' to sign out

    Your choice:"""

    def handler(self, user_choice):
        if user_choice == 1:
            return personal_passwords.PersonalPasswordsMenu(self.user)
        elif user_choice == 2:
            return team_passwords.TeamPasswordsMenu(self.user)
        elif user_choice == 3:
            Authorizer.sign_out()
            return authentication.AuthenticationMenu
        raise ValueError("Invalid Choice.")
