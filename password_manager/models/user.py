from utils.helpers.enums import UserType


class User:
    """
    User model which contains all the user's public details.
    """

    def __init__(self, user_id: str, user_type: int, username: str) -> None:
        self.__user_id = user_id
        self.user_type = UserType(user_type).name
        self.username = username

    @staticmethod
    def from_database(user_data: tuple):
        return User(
            user_id=user_data[0],
            user_type=user_data[3],
            username=user_data[1],
        )