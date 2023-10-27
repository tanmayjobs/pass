"""
This file defines a parent class for those menu classes which requires a team(such as Team Management Menu).
"""

class TeamRequiredMenu:

    def __init__(self, team) -> None:
        self.team = team
