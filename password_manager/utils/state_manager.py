from sqlite3 import IntegrityError

from utils.helpers.menu_prompts import AuthenticationMenu, MainMenu
from utils.helpers.exceptions import InvalidCredentials
from utils.show_message import show_message

from models.user import User
import sys

class StateManager:
    current_user: User | None = None
    current_prompt = MainMenu

    @staticmethod
    def run():
        while True:
            while not StateManager.current_user:
                try:
                    user_choice = int(input(AuthenticationMenu.prompt))
                    user = AuthenticationMenu.handler(user_choice)

                    StateManager.current_user = user
                    StateManager.current_prompt = MainMenu
                    break

                except ValueError:
                    show_message("Invalid Choice.")

                except InvalidCredentials:
                    show_message("Invalid username or password.")

                except IntegrityError:
                    show_message("Username already exists.")

                except SystemExit:
                    show_message("Bye.")
                    sys.exit(0)

            show_message(f"Successfully signed in as {StateManager.current_user.username}...")

            while StateManager.current_user:
                try:
                    user_choice = int(input(StateManager.current_prompt.prompt))
                    StateManager.current_prompt = StateManager.current_prompt.handler(user_choice, StateManager.current_user)

                    if StateManager.current_prompt == AuthenticationMenu:
                        StateManager.current_user = None
                        break

                except ValueError:
                    show_message("Invalid Choice.")

                except SystemExit:
                    show_message("Bye.")
                    sys.exit(0)

