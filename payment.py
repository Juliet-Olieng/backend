
class Payments:
    def __init__(self,customer,amount,phoneNumber) :
        self.customer=customer
        self.amount=amount
        self.phoneNumber=phoneNumber
#create a dictionary of the order attribute and returns it
    def add_payments(self):
        Payments={
           "customer":self.customer,
           "amount":self.amount,
           "phoneNumber":self.phoneNumber,
       }
        return Payments
# Prompts the user to input their details
customer=input("input your customer name: ")
amount=input("Input the amount: ")
phoneNumber=input("Input phonenumber: ")
# An instance of order is assigned to a variable called user
new_Customer=Payments(customer,amount,phoneNumber)
user=new_Customer
print(new_Customer.add_payments())