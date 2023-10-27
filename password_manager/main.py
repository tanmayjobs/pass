"""
This file contains the entry point to the application.
This file is responsible to start the Database core.
"""

from database.db import SQLDatabase
from utils.state_manager import StateManager
from logs.logger import Logger, INFO

if __name__ == "__main__":
    Logger.log(INFO, "Initializing System...")
    SQLDatabase.initialize()
    StateManager.run()
