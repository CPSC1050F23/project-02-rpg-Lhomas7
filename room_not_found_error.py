class RoomNotFoundError(Exception):
    def __init__(self, message = 'room not found'):
        self.message = message
    def __str__(self, user_exit):
        return f"Invalid room: {user_exit} -> {self.message}"