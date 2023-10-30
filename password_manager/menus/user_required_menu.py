"""
This file defines a parent class for those menu classes which requires a user(any menu other than authentication menu).
"""


class UserRequiredMenu:

    def __init__(self, user) -> None:
        self.user = user
