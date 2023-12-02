class Inventory:
    def __init__(self):
        self.inventory = {}
    def add_inventory(self,item_name,item_description):
        self.inventory[item_name] = item_description
    def print_inventory(self):
        print('INVENTORY:')
        for item in list(self.inventory.keys()):
            print(f'\t{item}-{self.inventory[item]}')
    def get_inventory(self):
        return self.inventory
        

            

