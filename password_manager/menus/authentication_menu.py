from controllers.authorizer import Authorizer

from utils.io_functions import show_message

class AuthenticationMenu:
    prompt = """
    Press:
    - '1' to sign in
    - '2' to sign up as user
    - '3' to sign up as team manager
    - '4' to exit

    Your choice:"""

    @staticmethod
    def handler(user_choice):
        if user_choice == 1:
            user = Authorizer.sign_in()
            return user

        elif user_choice == 2 or user_choice == 3:
            user_role = 0 if user_choice == 3 else 1
            Authorizer.sign_up(user_role)

            show_message("User created successfuly.")

        elif user_choice == 4:
            raise SystemExit

        else:
            raise ValueError("Invalid Choice.")

