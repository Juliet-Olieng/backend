
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_cart(self):
        return self.cart
    def add_to_cart(self, product):
        self.cart.append(product)
        return "Product added to cart successfully"
    def place_order(self):
        if not self.cart:
            return "Cart is empty"
        order_total = sum(product["price"] for product in self.cart)
        order = {"customer": self.name, "email": self.email, "total": order_total}
        self.cart = []
        return order
customer = Customer("John Doe", "johndoe@example.com")
print(customer.get_name())      # Output: John Doe
print(customer.get_email())     # Output: johndoe@example.com
customer.add_to_cart("Apple")
customer.add_to_cart("Banana")
print(customer.get_cart())      # Output: ['Apple', 'Banana']
order = customer.place_order()
print(order)                    # Output: {'customer': 'John Doe', 'email': 'johndoe@example.com', 'total': 0}
print(customer.get_cart())      # Output: []