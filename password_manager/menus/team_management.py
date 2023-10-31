"""
This file contains the Team Management Menu
Here user can manage any one previously selected team from Teams Password Menu.
"""

import controllers.password as PasswordController
import controllers.teams as TeamsController

from models.password import PasswordType

from utils.io_functions import show_message, show_passwords, create_password_input, select_by_id, team_member_username_input, show_members

import menus.user_required_menu as user_required_menu
import menus.team_required_menu as team_required_menu
import menus.teams_management as teams_management


class TeamManagementMenu(user_required_menu.UserRequiredMenu,
                         team_required_menu.TeamRequiredMenu):

    def __init__(self, user, team) -> None:
        user_required_menu.UserRequiredMenu.__init__(self, user)
        team_required_menu.TeamRequiredMenu.__init__(self, team)

    prompt = """
    Press:
    - '1' to add team member
    - '2' to remove team member
    - '3' to add password
    - '4' to delete password
    - '5' to update password
    - '6' to go back

    Your choice:"""

    def handler(self, user_choice):
        if user_choice == 1:
            member_name = team_member_username_input()
            TeamsController.add_member(self.user, self.team, member_name)
            show_message("Member added successfully.")

        elif user_choice == 2:

            if not self.team.members():
                show_message("No Member to delete.")

            else:
                members = self.team.members()

                if len(members) == 1:
                    show_message(
                        "There are no members in your team, except you.")

                else:
                    all_members = self.team.members()
                    show_members(all_members)
                    member_id = select_by_id(all_members, "member").user_id
                    TeamsController.delete_member(self.user, self.team, member_id)
                    show_message("Member deleted successfully.")

        elif user_choice == 3:
            site_url, site_username, password, notes = create_password_input()
            PasswordController.add_password(self.user, site_url, site_username, password, notes, self.team)
            show_message("Password added successfully.")

        elif user_choice == 4 or user_choice == 5:
            passwords = PasswordController.get_passwords(
                self.user,
                team=self.team,
                password_type=PasswordType.TEAM_PASSWORD,
            )

            if not passwords:
                show_message(f"No passwords to show.")

            else:
                show_passwords(passwords)

                if user_choice == 4:
                    password = select_by_id(passwords, "password")
                    PasswordController.delete_password(password)
                    show_message("Password deleted successfully.")

                else:
                    password = select_by_id(passwords, "password")
                    password_data = create_password_input()
                    PasswordController.update_password(password, *password_data)
                    show_message("Password updated successfully.")

        elif user_choice == 6:
            return teams_management.TeamsManagementMenu(self.user)

        else:
            raise ValueError

        return self
