class InventoryItem:
    def __init__(self, product_name, product_price, product_quantity):
        self.name=product_name
        self.price= product_price 
        self.quantity = product_quantity
    def add_inventory(self):
        inventory_dict={
           "name":self.product_name,
           "order":self.product_price,
           "payment":self.product_quantity,
       
       }
        return inventory_dict
product_name=input("input your name: ")
product_price=input("Input the type of order: ")
product_quantity=input("Input the type of payment: ")

new_Customer=InventoryItem(product_name,product_price,product_quantity)
user=new_Customer
print(new_Customer.add_inventory())

