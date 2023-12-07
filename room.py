#define the room class to hold a room's description, name, and exits
class Room:
    #initializes code, gets the name, description, and exits, and also returns the room in a string.
    def __init__(self, name = '', description = '', exits = [], items = []):
        self.name = name
        self.description = description
        self.exits = exits
        self.str_exit = ''
        self.items = items
        self.item_descriptions = {}
        self.list_items = []
    #returns the name of the room
    def get_name(self):
        return self.name
    #returns the description of the room
    def get_description(self):
        return self.description
    #returns the exits of the room
    def get_exits(self):
        return self.exits
    #returns each item in the room's description
    def get_item_descriptions(self):
        for item in self.items:
            self.item_descriptions[item.get_item()] = item.get_description()
        return self.item_descriptions
    #returns a list version of the room's exits
    def list_exits(self):
        for room in self.exits:
            self.str_exit += str(room)
            self.str_exit += '\n'
        return self.str_exit
    #returns the string of the room and its description
    def __str__(self):
        room_des = f"{self.name}: {self.description}\n\nExits:\n{self.str_exit}"
        return room_des
    #returns the room's descrption specified for the action lookaround
    def lookaround_room(self):
        room_des = f'{self.description}'
        return room_des
    #returns the items in the room
    def get_items(self):
        return self.items
    #removes an item from the list of items and returns that list
    def remove_item(self):
        self.list_items = self.list_items.remove(self.list_items[0])
        return self.list_items
    #returns a list of items in the room
    def get_item_list(self):
        list_items = []
        for item in self.items:
            list_items.append(item.get_item())
        self.list_items = list_items
        return self.list_items