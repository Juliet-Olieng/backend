
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return(f"{item} added to cart")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return(f"{item} removed from cart")
        else:
            return(f"{item} not found in cart")
            

    def view_cart(self):
        if len(self.items) == 0:
            return("Cart is empty")
        else:
            return("Cart contains:")
            for item in self.items:
                return(item)
# cart=ShoppingCart()
# cart.add_item("apple")
# cart.remove_item("apple")
# cart.view_cart()