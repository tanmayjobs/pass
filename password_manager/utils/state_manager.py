from models.user import User

class StateManager:
    def __init__(self) -> None:
        self.current_user: User | None = None
