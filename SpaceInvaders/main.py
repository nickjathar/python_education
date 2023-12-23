# define a class
class Item:
    # constructor (__init__ is a magic method)
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to 0!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to 0!"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

# create an instance of a class
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(item1.name, item2.name)
print(item1.calculate_total_price(), item2.calculate_total_price())

item2.has_numpad = True

print(item2.has_numpad)
