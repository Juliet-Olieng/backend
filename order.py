class Orders:
    def __init__(self,Name,order,payment) :
        self.order=order
        self.Name=Name
        self.payment=payment
      
#create a dictionary of the order attribute and returns it
    def add_order(self):
        orders_dict={
           "name":self.Name,
           "order":self.order,
           "payment":self.payment,
       
       }
        return orders_dict
# Prompts the user to input their details
Name=input("input your name: ")
order=input("Input the type of order: ")
payment=input("Input the type of payment: ")


# An instance of order is assigned to a variable called user
new_Customer=Orders(Name,order,payment)
user=new_Customer
print(new_Customer.add_order())
