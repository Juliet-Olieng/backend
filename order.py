class Orders:
    def __init__(self,customer_name,order_placed,means_of_payment) :
        self.customer_name=customer_name
        self.order_placed=order_placed
       
        self.means_of_payment=means_of_payment
      
#create a dictionary of the order attribute and returns it
    def add_order(self):
        orders_dict={
           "customer_name":self.customer_name,
           "order_placed":self.order_placed,
           "means_of_payment":self.means_of_payment,
       
       }
        return orders_dict
# Prompts the user to input their details
customer_name=input("input your name: ")
order_placed=input("Input the type of order: ")
means_of_payment=input("Input the type of payment: ")


# An instance of order is assigned to a variable called user
new_Customer=Orders(customer_name,order_placed,means_of_payment)
user=new_Customer
print(new_Customer.add_order())
