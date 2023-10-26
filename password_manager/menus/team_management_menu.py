from controllers.password_controller import PasswordController
from controllers.teams_controller import TeamsController

from models.password import PasswordType

from utils.io_functions import show_message, show_passwords

import menus.user_required_menu as user_required_menu
import menus.team_required_menu as team_required_menu
import menus.teams_management_menu as teams_management_menu


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
            TeamsController.add_member(self.user, self.team)
            show_message("Member added successfully.")
        elif user_choice == 2:
            if not self.team.members():
                show_message("No Member to delete.")
            else:
                TeamsController.delete_member(self.team)
                show_message("Member deleted successfully.")
        elif user_choice == 3:
            PasswordController.add_password(self.user, self.team)
            show_message("Password added successfully.")
        elif user_choice == 4 or user_choice == 5:
            passwords = PasswordController.get_passwords(
                self.user,
                password_type=PasswordType.TEAM_PASSWORD,
            )

            if not passwords:
                show_message(f"You haven't saved any password yet.")
            else:
                show_passwords(passwords)
                if user_choice == 4:
                    PasswordController.delete_password(self.user, passwords)
                    show_message("Password deleted successfully.")
                else:
                    PasswordController.update_password(self.user, passwords)
                    show_message("Password updated successfully.")
        elif user_choice == 6:
            return teams_management_menu.TeamsManagementMenu(self.user)
        else:
            raise ValueError
        return self
