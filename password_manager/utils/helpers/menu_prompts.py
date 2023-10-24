from handlers.before_auth.authentication_handler import AuthenticationHandler

from utils.show_message import show_message
class AuthenticationMenu:
    prompt = """
    Press:
    - '1' for sign in
    - '2' for sign up as user
    - '3' for sign up as team manager
    - '4' for exit

    Your choice:"""

    @staticmethod
    def handler(user_choice):
        if user_choice == 1:
            user = AuthenticationHandler.sign_in()
            return user

        elif user_choice == 2 or user_choice == 3:
            user_role = 0 if user_choice == 3 else 1

            user = AuthenticationHandler.sign_up(user_role)
            return user

        elif user_choice == 4:
            raise SystemExit

        raise ValueError("Invalid Choice.")


class MainMenu:
    prompt = """
    Press:
    - '1' for personal passwords
    - '2' for team passowrds
    - '3' for sign out

    Your choice:"""

    @staticmethod
    def handler(user_choice):
        if user_choice == 1:
            ...
        elif user_choice == 2:
            ...
        elif user_choice == 3:
            AuthenticationHandler.sign_out()
            return AuthenticationMenu
        raise ValueError("Invalid Choice.")

