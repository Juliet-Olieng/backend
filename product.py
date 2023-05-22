
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def update_stock(self, quantity):
        self.stock += quantity
        if self.stock < 0:
            self.stock = 0

    def is_available(self):
        return self.stock > 0

    def purchase(self, quantity):
        if self.is_available():
            if quantity <= self.stock:
                self.update_stock(-quantity)
                return f"Purchased {quantity} {self.name}"
            else:
                return f"Insufficient stock for {self.name}"
        else:
            return f"{self.name} is out of stock"


# Example usage
apple = Product("Apple", 1.99, 10)

print(apple.get_name())      # Output: Apple
print(apple.get_stock())     # Output: 10

apple.update_stock(-3)
print(apple.get_stock())     # Output: 7

print(apple.is_available())  # Output: True

print(apple.purchase(5))    # Output: Purchased 5 Apple(s)
print(apple.get_stock())     # Output: 2

print(apple.purchase(10))   # Output: Insufficient stock for Apple
print(apple.get_stock())     # Output: 2

apple.update_stock(5)
print(apple.get_stock())     # Output: 7
