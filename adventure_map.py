from room import Room
from room_not_found_error import RoomNotFoundError

class AdventureMap:
    #initializes the map, defines how to add a room and go to a room in the map.
    def __init__(self, room = Room(), error = RoomNotFoundError()):
        self.map = {}
        self.error = error
        self.room = room
        self.room_exits = {}
        self.rooms = []  
        self.items = {}
        self.inv_items = {}
        self.item_description = {}
        self.item_get_content = {}    
        self.room_descriptions = {}
        self.room_item_description = {}
        self.item_actions = {}
        self.room_item_content = {}
        self.rooms_names = {}
    def add_room(self, room_layout):
        self.room = room_layout
        self.room.list_exits()
        self.map[self.room.get_name()] = self.room.__str__()
        self.room_exits[self.room.get_name()] = self.room.get_exits()
        self.rooms.append(room_layout)
        self.items[self.room.get_name()] = self.room.string_of_items(self.room.list_of_items())
        self.inv_items[self.room.get_name()] = self.room.list_of_items()
        self.room_descriptions[self.room.get_name()] = self.room.lookaround_room()
        self.room_item_description[self.room.get_name()] = self.room.get_item_descriptions()
        for item in self.room.list_of_items():
            self.item_actions[item] = self.room.get_item_actions()[item]
            self.room_item_content[item] = self.room.get_item_contents()[item]
        self.rooms_names[self.room.get_name()] = self.room
    def get_room(self, user_room):
        key_list = list(self.map.keys())
        count = 0
        for key in key_list:
            if user_room.lower() == key.lower():
                return self.map[key]
                user_room = key
                count += 1
    def get_list_items(self, room):
        return self.inv_items[room]
    def get_item_actions(self,item_name):
        return self.item_actions[item_name]#edited
    def get_item_description(self,item_name,room):
        return self.room_item_description[room][item_name]
    def get_item_content(self, item_name):#edited
        return self.room_item_content[item_name]
    def get_room_items(self,room):
        return self.items[room]
    def get_room_exits(self,room):
        return self.room_exits[room]
    def get_room_description(self,room):
        return self.room_descriptions[room]
    def get_items(self):
        return self.room.get_items
    def remove_item(self,room_name):
        for room in list(self.rooms_names.keys()):
            if room == room_name:
                self.rooms_names[room_name].remove_item()
    def get_new_list(self,room_name):
        for room in list(self.rooms_names.keys()):
            if room == room_name:
                return self.rooms_names[room_name].list_of_items()

        

