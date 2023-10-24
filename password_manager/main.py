from database.db import SQLDatabase
from utils.state_manager import StateManager

if __name__ == "__main__":
    SQLDatabase.initialize()
    
    state_manager = StateManager()
    state_manager.run()
