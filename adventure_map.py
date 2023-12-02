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
    def add_room(self, room_layout):
        self.room = room_layout
        self.room.list_exits()
        self.map[self.room.get_name()] = self.room.__str__()
        self.room_exits[self.room.get_name()] = self.room.get_exits()
        self.rooms.append(room_layout)
        self.items[self.room.get_name()] = self.room.string_of_items()
        self.inv_items[self.room.get_name()] = self.room.list_of_items()
        self.item_description[]
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
        return self.room.get_item_actions()[item_name]
    def get_item_description(self,item_name):
        return self.room.get_item_descriptions()[item_name]
    def get_item_content(self, item_name):
        return self.room.get_item_contents()[item_name]
    def get_room_items(self,room):
        return self.items[room]
    def get_room_exits(self,room):
        return self.room_exits[room]