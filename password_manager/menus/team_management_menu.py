from utils.io_functions import team_add_member_input

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
            member_username = team_add_member_input()
            raise NotImplementedError
        elif user_choice == 2:
            raise NotImplementedError
        elif user_choice == 3:
            raise NotImplementedError
        elif user_choice == 4:
            raise NotImplementedError
        elif user_choice == 5:
            raise NotImplementedError
        elif user_choice == 6:
            return teams_management_menu.TeamsManagementMenu(self.user)
        else:
            raise ValueError
