class Team:
    """
    Team model which contains all the team's details,
    including all the passwords, creator and members of team.
    """

    def __init__(self, team_id: str, creator_id: str, team_name: str) -> None:
        self.team_id = team_id
        self.creator_id = creator_id
        self.team_name = team_name

    @staticmethod
    def from_database(team_data: tuple) -> "Team":
        return Team(*team_data)

    def __repr__(self) -> str:
        return f"{self.team_name:20}"
