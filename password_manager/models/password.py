from utils.helpers.enums import PasswordType


class Password:
    """
    Password model which contains the details of password.
    """

    def __init__(
        self,
        password_id: str,
        creator: str,
        password_type: PasswordType,
        site_url: str,
        username: str,
        encrypted_password: str,
        notes: str,
    ) -> None:
        self.__password_id = password_id
        self.creator = creator
        self.password_type = password_type
        self.site_url = site_url
        self.username = username
        self.encrypted_password = encrypted_password
        self.notes = notes
