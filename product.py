class ItemsAvailable:
    def __init__(self,item_name,price,addtocart, available_groceries) :
        self.item_name=item_name
        self.price=price
        self.addtocart=addtocart
        self.groceries = available_groceries
    def add_item(self):
        self.add=self.addtocart
#Checking if the item selection is available in stock
        if self.item_name in self.groceries and self.price in self.groceries:
            self.item_name==True
            return(f"{self.item_name} added to basket")
        else:
            self.item_name == False
            return(f"{self.item_name} is not available")
        
    print(add_item("mango"))
    
# returning the final state of the button "add to cart"
        # return self.add
# use example
# item = ItemsAvailable("pineapple", 200, True, {"pineapple": 180, "mango": 100})
# print(item.add_item(True))
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
                return f"Purchased {quantity} {self.name}(s)"
            else:
                return f"Insufficient stock for {self.name}"
        else:
            return f"{self.name} is out of stock"


# # Example usage
# apple = Product("Apple", 1.99, 10)

# print(apple.get_name())      # Output: Apple
# print(apple.get_stock())     # Output: 10

# apple.update_stock(-3)
# print(apple.get_stock())     # Output: 7

# print(apple.is_available())  # Output: True

# print(apple.purchase(5))    # Output: Purchased 5 Apple(s)
# print(apple.get_stock())     # Output: 2

# print(apple.purchase(10))   # Output: Insufficient stock for Apple
# print(apple.get_stock())     # Output: 2

# apple.update_stock(5)
# print(apple.get_stock())     # Output: 7
