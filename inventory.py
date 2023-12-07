#create Inventory class to store user inventory items
class Inventory:
    #initialize inventory
    def __init__(self):
        self.inventory = []
        self.item = None
    #define how to add items to inventory
    def add_inventory(self,item):
        self.inventory.append(item)
    #define how to print the inventory
    def print_inventory(self):
        print('INVENTORY:')
        for item in self.inventory:
            print(f'\t  {item.get_item()}- {item.get_description()}')
    #define how to return inventory
    def get_inventory(self):
        return self.inventory
        

            

