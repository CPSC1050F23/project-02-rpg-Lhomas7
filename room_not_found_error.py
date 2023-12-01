class RoomNotFoundError(Exception):
    def __init__(self, message = 'room not found'):
        self.message = message
    def __str__(self,exit):
        return f"{exit} -> {self.message}"