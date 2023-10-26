from utils.exception_handler import handle_exception
from menus.authentication_menu import AuthenticationMenu
from menus.main_menu import MainMenu
from utils.io_functions import show_message

from models.user import User

class StateManager:
    current_user: User | None = None
    current_prompt = MainMenu

    @handle_exception
    @staticmethod
    def before_auth():
        user_choice = int(input(AuthenticationMenu.prompt))
        user = AuthenticationMenu.handler(user_choice)

        if not user:
            return

        StateManager.current_user = user
        StateManager.current_prompt = MainMenu(user)

    @handle_exception
    @staticmethod
    def after_auth():
        user_choice = int(input(StateManager.current_prompt.prompt))
        StateManager.current_prompt = StateManager.current_prompt.handler(user_choice)

        if StateManager.current_prompt == AuthenticationMenu:
            StateManager.current_user = None

    @staticmethod
    def run():
        while True:
            while not StateManager.current_user:
                StateManager.before_auth()

            show_message(
                f"Successfully signed in as {StateManager.current_user.username}..."
            )

            while StateManager.current_user:
                StateManager.after_auth()

            show_message("You're logged out of the system.")
