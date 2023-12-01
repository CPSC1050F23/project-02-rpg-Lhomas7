#define the room class to hold a room's description, name, and exits
class Room:
    #initializes code, gets the name, description, and exits, and also returns the room in a string.
    def __init__(self, name = '', description = '', exits = [], items = []):
        self.name = name
        self.description = description
        self.exits = exits
        self.str_exit = ''
        self.items = items
        self.str_items = ''
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_exits(self):
        return self.exits
    def string_of_items(self):
        for item in self.items:
            self.str_items += item.get_item()
            self.str_items += ' '
        return self.str_items
    def list_exits(self):
        for room in self.exits:
            self.str_exit += str(room)
            self.str_exit += '\n'
        return self.str_exit       
    def __str__(self):
        room_des = f"{self.name}: {self.description}\n\nExits:\n{self.str_exit}"
        return room_des
    def get_items(self):
        return self.items