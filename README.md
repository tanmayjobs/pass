# Password Manager

Password Manager is a simple command-line tool for securely storing and managing your passwords. This repository contains the source code for the password manager application.

## Getting Started

To run the program, you will need to set up a `.env` file containing your encryption key. Please follow these steps to get started:

1. Clone this repository to your local machine.

2. Change directory to `password_manager/password_manager/`.

3. Open your terminal and execute the following Python code to generate an encryption key:

```python
from cryptography.fernet import Fernet

key = str(Fernet.generate_key())
with open('.env', 'w+') as env_file:
    env_file.write(f'KEY={key[1:]}')

```
4. Run the program using python main.py
