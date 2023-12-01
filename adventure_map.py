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
    def add_room(self, room_layout):
        self.room = room_layout
        self.room.list_exits()
        self.map[self.room.get_name()] = self.room.__str__()
        self.room_exits[self.room.get_name()] = self.room.get_exits()
        self.rooms.append(room_layout)
    def get_room(self, user_room):
        key_list = list(self.map.keys())
        count = 0
        for key in key_list:
            if user_room.lower() == key.lower():
                return self.map[key]
                user_room = key
                count += 1
    def get_room_exits(self,room):
        for item in self.rooms:
            if item.get_name() == room:
                return self.rooms[item].get_exits()
