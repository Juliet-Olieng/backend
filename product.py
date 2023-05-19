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