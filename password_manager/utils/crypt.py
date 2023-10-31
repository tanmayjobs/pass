"""
This file contains all cryptography methods.
    Hash
    Check
    Encrypt
    Decrypt
"""

import os
import dotenv
import bcrypt
from cryptography.fernet import Fernet

dotenv.load_dotenv()


class Crypt:

    @staticmethod
    def hash(password: str) -> str:
        password_bytes = password
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)

        return password_hash

    @staticmethod
    def check(password: str, hashed_password: str):
        return bcrypt.checkpw(password, hashed_password)

    @staticmethod
    def encrypt(password: str):
        key = os.getenv("KEY")
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(password.encode())
        return encrypted_password

    @staticmethod
    def decrypt(encrypted_password: str):
        key = os.getenv("KEY")
        fernet = Fernet(key)
        decrypted_password = fernet.decrypt(encrypted_password).decode()
        return decrypted_password
