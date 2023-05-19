
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to cart")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} removed from cart")
        else:
            print(f"{item} not found in cart")
            

    def view_cart(self):
        if len(self.items) == 0:
            print("Cart is empty")
        else:
            print("Cart contains:")
            for item in self.items:
                print(item)
cart=ShoppingCart()
cart.add_item("apple")
cart.remove_item("apple")
cart.view_cart()