class Inventory:
    def __init__(self):
        self.inventory = []
    def add_inventory(self,item):
        self.inventory.append(item)
    def print_inventory(self):
        print('INVENTORY:')
        for item in self.inventory:
            print(f'\t{item}-{adventure_map.get_item_description(item)}')
    def get_inventory(self):
        return self.inventory
        

            

