"""
All the custom exceptions are defined here.
"""

class UserNotFound(Exception):
    ...


class InvalidCredentials(Exception):
    ...


class NullPassword(Exception):
    ...


class WeakPassword(Exception):
    ...


class NullUsername(Exception):
    ...


class InvalidMemberName(Exception):
    ...


class MemberAlreadyExists(Exception):
    ...


class UserRemovingSelf(Exception):
    ...
