class InventoryItem:
    def __init__(self, product_name, product_price, product_quantity):
        self.product_name=product_name
        self.product_price= product_price
        self.product_quantity = product_quantity
    def add_inventory(self):
        inventory_dict={
           "product_name":self.product_name,
           "product_price":self.product_price,
           "product_quantity":self.product_quantity,
       }
        return inventory_dict
# product_name=input("input product name: ")
# product_price=input("Input the price of the product: ")
# product_quantity=input("Input the quantity of the products: ")
# new_Customer=InventoryItem(product_name,product_price,product_quantity)
# user=new_Customer
# print(new_Customer.add_inventory())

