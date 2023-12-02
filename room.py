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
        self.item_descriptions = {}
        self.item_contents = {}
        self.item_actions = {}
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_exits(self):
        return self.exits
    def list_of_items(self):
        item_list = []
        for item in self.items:
            item_list.append(item.get_item())
        return item_list
    def string_of_items(self):
        first_item = True
        for item in self.items:
            if first_item:
                first_item = False
                self.str_items += item.get_item()
                continue
            self.str_items += ', '
            self.str_items += item.get_item()
        return self.str_items
    def get_item_descriptions(self):
        for item in self.items:
            self.item_descriptions[item.get_item()] = item.get_description()
        return self.item_descriptions
    def get_item_contents(self):
        for item in self.items:
            self.item_contents[item.get_item()] = item.get_item_content()
        return self.item_contents
    def list_exits(self):
        for room in self.exits:
            self.str_exit += str(room)
            self.str_exit += '\n'
        return self.str_exit
    def get_item_actions(self):
        for item in self.items:
            self.item_actions[item.get_item()] = item.get_action()
        return self.item_actions
    def __str__(self):
        room_des = f"{self.name}: {self.description}\n\nExits:\n{self.str_exit}"
        return room_des
    def lookaround_room(self):
        room_des = f'{self.description}'
        return room_des
    def get_items(self):
        return self.items