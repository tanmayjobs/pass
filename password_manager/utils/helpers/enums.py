from enum import Enum


class PasswordType(Enum):
    """
    Differentiate the password types:
        1.Personal Passwords
        2.Team Passwords
    """
    PERSONAL_PASSWORD = 0
    TEAM_PASSWORD = 1


class UserType(Enum):
    """
    Differentiate the user types:
        1.Admin User
        2.Basic User
    """
    ADMIN_USER = 0
    BASIC_USER = 1
