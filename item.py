class Item:
    def __init__(self, name, description, item_content):
        self.name = name
        self.description = description
        self.item_content = item_content
        self.action = None
    def get_item(self):
        return self.name
    def get_description(self):
        return self.description
    def get_item_content(self):
        return self.item_content
    def set_action(self, action):
        self.action = action
    def set_item_content(self, content):
        self.item_content = content
    def get_action(self):
        return self.action
    
