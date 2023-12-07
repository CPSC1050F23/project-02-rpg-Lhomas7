from room import Room
from room_not_found_error import RoomNotFoundError
#AdventureMap class to store all of the rooms items and actions the user can take
class AdventureMap:
    #initializes the map, defines creates a map dictionary and other dictionaries for storing rooms, items, and their attributes
    def __init__(self, room = Room(), error = RoomNotFoundError()):
        self.map = {}
        self.error = error
        self.room = room
        self.room_exits = {}
        self.rooms = []  
        self.items = {}  
        self.room_descriptions = {}
        self.room_item_description = {}
        self.room_items = {}
        self.str_items = ''
    #adds the appropraite room and item descriptions to their respective dictionaries and adds a room to the map
    def add_room(self, room_layout):
        self.room_items[self.room.get_name()] = self.room.get_items()
        self.room = room_layout
        self.room.list_exits()
        self.map[self.room.get_name()] = self.room.__str__()
        self.room_exits[self.room.get_name()] = self.room.get_exits()
        self.rooms.append(room_layout)
        self.room_descriptions[self.room.get_name()] = self.room.lookaround_room()
        self.room_item_description[self.room.get_name()] = self.room.get_item_descriptions()
    #returns a room given its name
    def get_room(self, user_room):
        key_list = list(self.map.keys())
        count = 0
        for key in key_list:
            if user_room.lower() == key.lower():
                return self.map[key]
                user_room = key
                count += 1
    #returns a room's exits
    def get_room_exits(self,room):
        return self.room_exits[room]
    #returns a room's description
    def get_room_description(self,room):
        return self.room_descriptions[room]
    #get the items from a room
    def get_items(self):
        return self.room.get_items
    #removes an item from the room
    def remove_item(self,room_name):
        self.room_items[room_name].remove(self.room_items[room_name][0])
    #returns a string of items to be included in the room description
    def get_string_of_items(self, room_name):
        self.str_items = ''
        first_item = True
        for item in self.room_items[room_name]:
            if first_item:
                first_item = False
                self.str_items += item.get_item()
                continue
            self.str_items += ', '
            self.str_items += item.get_item()
        return self.str_items
    #returns the items held in a specified room
    def get_rooms_and_items(self,room_name):
        return self.room_items[room_name]

        

