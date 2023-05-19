
class Payments:
    def __init__(self,customer,amount,phoneNumber) :
        self.customer=customer
        self.amount=amount
        self.phoneNumber=phoneNumber
#create a dictionary of the order attribute and returns it
    def add_payments(self):

        return f"{self.customer}has paid{self.amount}through{self.phoneNumber}"
    
def generate_payment_receipt(payment_details, transaction_id):
    # Assuming payment_details is a dictionary with relevant information
    # Assuming transaction_id is a string representing the transaction ID
    
    receipt = "Payment Receipt\n"
    receipt += "Transaction ID: {}\n".format(transaction_id)
    receipt += "------------------------\n"
    receipt += "Payment Details:\n"
    receipt += "Amount: {}\n".format(payment_details['amount'])
    receipt += "Payment Method: {}\n".format(payment_details['payment_method'])
    receipt += "Date: {}\n".format(payment_details['date'])
    receipt += "------------------------\n"
    receipt += "Thank you for your payment!\n"
    
    return receipt


# Usage example
payment_details = {
    'amount': 100.00,
    'payment_method': 'Credit Card',
    'date': '2023-05-18'
}

transaction_id = 'ABC123XYZ'

receipt = generate_payment_receipt(payment_details, transaction_id)
print(receipt)
