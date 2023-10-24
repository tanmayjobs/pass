from database.db import SQLDatabase
from utils.state_manager import StateManager

if __name__ == "__main__":
    SQLDatabase.initialize()
    StateManager.run()
