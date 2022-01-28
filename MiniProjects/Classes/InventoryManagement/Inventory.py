


class Inventory:


    def __init__(self):
        self.inventory = []

    def add_item(self, *args):
        for arg in args:
            self.inventory.append(arg)
            print(f"{arg.name} added")

    def discount_all(self, amount):
        if amount in range(0,101):
            for item in self.inventory:
                item.value *= amount / 100
        return print(f"%{amount}")

    def show_inventory(self):
        for item in self.inventory:
            return print(f"ID: {item.pID} Name: {item.name} Value: {item.value} Quantity: {item.quantity}\n")

    def inventory_total(self):
        total_value = 0
        total_quantity = 0
        for item in self.inventory:
            total_value += item.value * item.quantity
            total_quantity += item.quantity
        return print(f"Total value: {total_value} Total quantity: {total_quantity}")

class Item:
    ID = 0

    def __init__(self, name:str, value:float, quantity:int):
        self.pID = Item.ID
        Item.ID += 1
        self.name = name
        self.value = value
        self.quantity = quantity

        return print(f"Object {self.name} created with ID {self.pID}")

    def update_quantity(self, q):
        self.quantity = q

    def change_value(self,v):
        self.value = v

class Fruit(Item):
    def __init__(self, name, value, quantity, CO, shelf_life):
        Item.__init__(self, name, value, quantity)
        self.country_origin = CO
        self.shelf_life = shelf_life

    def __str__(self):
        return f"Class: {__class__.__name__} Name: {self.name}"



inventory = Inventory()

orange = Fruit('orange', .99, 300,'Canada','3 weeks')
pen = Item('pen', 1.25, 100)

inventory.add_item(orange, pen)
inventory.inventory_total()

print(orange)