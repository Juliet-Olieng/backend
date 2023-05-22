class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
        return(f"{product} added to cart!")

    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)
            return(f"{product} removed from cart!")
        else:
            return(f"{product} is not in your cart.")

    def view_cart(self):
        if self.cart:
            return("Your cart:")
            for product in self.cart:
                print(product)
        else:
            return("Your cart is empty.")

    def checkout(self):
        if self.cart:
            return("Checking out...")
            # Additional logic for processing the checkout and payment can be added here
            self.cart = []
            return("Thank you for shopping with us!")
        else:
            return("Your cart is empty. Nothing to checkout.")

# Example usage:
# customer = Customer("Eunice Musenyia", "eunicemusenyia@gmail.com")
# customer.add_to_cart("Product 1")
# customer.add_to_cart("Product 2")
# customer.add_to_cart("Product 3")
# customer.view_cart()
# customer.remove_from_cart("Product 2")
# customer.view_cart()
# customer.checkout()

