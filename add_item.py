class add_item:
    def __init__(self, item_name, item_price, item_quantity):
        self.item_name=item_name
        self.item_price=item_price
        self.item_quantity =item_quantity
    def getItem(self):
          user_item= {
            "item_name": self.item_name,
            "item_price": self.item_price,
            "item_quantity": self.item_quantity,
        }
          return user_item
# item_name=input("input the product_name : ")
# item_price=input("Input the  price of the products: ")
# item_quantity=input("Input the quantity of the products: ")
#     # An instance of order is assigned to a variable called user
# new_Customer=add_item(item_name,item_price,item_quantity)
# user=new_Customer
# print(new_Customer.getItem())



