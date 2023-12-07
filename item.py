#define item class for picking up in rooms and adding to inventory
class Item:
    #initialize class
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.item_content = None
        self.action = None
    #define how to return the item name
    def get_item(self):
        return self.name
    #returns the item description
    def get_description(self):
        return self.description
    #returns the item content
    def get_item_content(self):
        return self.item_content
    #sets the action given by the main class
    def set_action(self, action):
        self.action = action
    #sets the item content provided by the main class
    def set_item_content(self, content):
        self.item_content = content
    #returns the item's action
    def get_action(self):
        return self.action
    
