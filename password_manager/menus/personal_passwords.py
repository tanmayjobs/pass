"""
This file contains the personal password menu.
Here user have choice to:
    List
    Search
    Add
    Delete
    Update
their personal passwords.
"""

from controllers.password import PasswordController

from utils.io_functions import show_passwords, show_message

import menus.user_required_menu as user_required_menu
import menus.home_menu as home_menu


class PersonalPasswordsMenu(user_required_menu.UserRequiredMenu):
    prompt = """
    Press:
    - '1' to list passwords
    - '2' to search password
    - '3' to add new password
    - '4' to delete password
    - '5' to update password
    - '6' to go back

    Your choice:"""

    def handler(self, user_choice):
        if user_choice == 1 or user_choice == 2 or user_choice == 4 or user_choice == 5:
            passwords = PasswordController.get_passwords(
                self.user, user_choice == 2)

            if not passwords:
                show_message(f"No passwords to show.")
            else:
                show_passwords(passwords)
                if user_choice < 3:
                    passwords = PasswordController.show_true_passwords(
                        passwords)
                    show_passwords(passwords, False)
                if user_choice == 4:
                    PasswordController.delete_password(self.user, passwords)
                    show_message("Password deleted successfuly.")
                elif user_choice == 5:
                    PasswordController.update_password(self.user, passwords)
                    show_message("Password updated successfuly.")

        elif user_choice == 3:
            PasswordController.add_password(self.user)
            show_message("Password added successfuly.")

        elif user_choice == 6:
            return home_menu.HomeMenu(self.user)

        else:
            raise ValueError("Invalid Choice.")

        return self
