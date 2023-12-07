#creates a class thrown when a room entered by the player is not valid
class RoomNotFoundError(Exception):
    #initializes the class
    def __init__(self, message = 'room not found'):
        self.message = message
    #returns a string message when called
    def __str__(self, user_exit):
        return f"Invalid room: {user_exit} -> {self.message}"