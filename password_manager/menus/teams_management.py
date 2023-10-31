"""
This file contains the Teams Management Menu, don't confuse it with Team Management Menu(Focus on the 's' in Team).
Here Team Managers can add or delete teams.
And can also select one particular team to manage(which is further managed in Team Management Menu ).
"""

import controllers.teams as TeamsController

from utils.io_functions import show_teams, show_message, create_team_input, select_by_id

import menus.user_required_menu as user_required_menu
import menus.team_passwords as team_passwords
import menus.team_management as team_management


class TeamsManagementMenu(user_required_menu.UserRequiredMenu):
    prompt = """
    Press:
    - '1' to add team
    - '2' to delete team
    - '3' to manage team
    - '4' to go back

    Your choice:"""

    def handler(self, user_choice):
        if user_choice == 1:
            team_name = create_team_input()
            TeamsController.add_team(self.user, team_name)
        elif user_choice == 2:
            teams = TeamsController.get_teams(self.user)
            if not teams:
                show_message("You haven't created any teams yet.")
            else:
                show_teams(teams)
                team = select_by_id(teams, "team")
                TeamsController.delete_team(teams, self.user)
                show_message("Team deleted successfully!")
        elif user_choice == 3:
            teams = TeamsController.get_teams(self.user)
            if not teams:
                show_message("You haven't created any teams yet.")
            else:
                show_teams(teams)
                team = select_by_id(teams, "team")
                show_message(f"Team {team.team_name} is selected.")
                return team_management.TeamManagementMenu(self.user, team)
        elif user_choice == 4:
            return team_passwords.TeamPasswordsMenu(self.user)
        else:
            raise ValueError("Invalid Choice.")

        return self
