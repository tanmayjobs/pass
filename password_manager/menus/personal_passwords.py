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

import controllers.password as PasswordController

from utils.io_functions import show_passwords, show_message, password_ids_input, create_password_input, select_by_id, search_key_input

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
            search_key = search_key_input() if user_choice == 2 else ""
            passwords = PasswordController.get_passwords(
                self.user,
                search_key= search_key,
            )

            if not passwords:
                show_message(f"No passwords to show.")
            else:
                show_passwords(passwords)
                if user_choice < 3:
                    user_input = password_ids_input()
                    passwords = PasswordController.show_true_passwords(passwords, user_input)
                    show_passwords(passwords, False)
                if user_choice == 4:
                    password = select_by_id(passwords, "password")
                    PasswordController.delete_password(password)
                    show_message("Password deleted successfuly.")
                elif user_choice == 5:
                    password = select_by_id(passwords, "password")
                    password_data = create_password_input()
                    PasswordController.update_password(password, *password_data)
                    show_message("Password updated successfuly.")

        elif user_choice == 3:
            site_url, site_username, password, notes = create_password_input()
            PasswordController.add_password(self.user, site_url, site_username, password, notes)
            show_message("Password added successfuly.")

        elif user_choice == 6:
            return home_menu.HomeMenu(self.user)

        else:
            raise ValueError("Invalid Choice.")

        return self
