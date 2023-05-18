class InventoryItem:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity =quantity
        
    def getItem(self):
          user_item= {
            "name": self.name,
            "email": self.price,
            "password": self.quantity,
           
        } 
          return user_item
name=input("input your name: ")
price=input("Input the type of price: ")
quantity=input("Input the quantity: ")

    # An instance of order is assigned to a variable called user
new_Customer=InventoryItem(name,price,quantity)
user=new_Customer
print(new_Customer.getItem())
        




