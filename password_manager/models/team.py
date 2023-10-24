from models.user import User


class Team:
    """
    Team model which contains all the team's details,
    including all the passwords, creator and members of team.
    """

    def __init__(
        self,
        team_id: str,
        creator: User,
        team_name: str,
        team_members: [User],
    ) -> None:
        self.__team_id = team_id
        self.creator = creator
        self.team_name = team_name
        self.team_members = team_members
