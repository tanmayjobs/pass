from models.password import Password
from models.team import Team
from utils.helpers.enums import UserType


class BaseUser:
    """
    User model which contains all the user's public details.
    """

    def __init__(self, user_id: str, user_type: UserType, username: str) -> None:
        self.__user_id = user_id
        self.user_type = user_type
        self.username = username


class User(BaseUser):
    """
    User model which contains all the user's details,
    including all the passwords he or she have.
    """

    def __init__(
        self,
        user_id: str,
        user_type: UserType,
        username: str,
        passwords: list[Password],
        teams: list[Team],
    ) -> None:
        super(BaseUser, self).__init__(self, user_id, user_type, username)
        self.__passwords = passwords
        self.__teams = teams
