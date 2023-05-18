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
# Create a Product instance
apple = Product("Apple", 1.99, 10)

# Retrieve the name, price, and stock of the product
print(apple.get_name())    # Output: Apple
print(apple.get_price())   # Output: 1.99
print(apple.get_stock())   # Output: 10

# Update the stock of the product
apple.update_stock(-2)     # Reduce stock by 2

# Retrieve the updated stock of the product
print(apple.get_stock())   # Output: 8