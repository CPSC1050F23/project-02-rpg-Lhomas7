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
    def add_room(self, room_layout):
        self.room = room_layout
        self.room.list_exits()
        self.map[self.room.get_name()] = self.room.__str__()
        self.room_exits[self.room.get_name()] = self.room.get_exits()
        self.rooms.append(room_layout)
        self.items[self.room.get_name()] = self.room.list_items()
    def get_room(self, user_room):
        key_list = list(self.map.keys())
        count = 0
        for key in key_list:
            if user_room.lower() == key.lower():
                return self.map[key]
                user_room = key
                count += 1
    def get_room_items(self,room):
        return self.items[room]
        
    def get_room_exits(self,room):
        return self.room_exits[room]