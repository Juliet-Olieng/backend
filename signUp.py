class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password=password
    def sign_up(self):#returns the dictionary containing the user information
        signup= {
            "name": self.name,
            "email": self.email,
            "password": self.password,
         
        }
        return signup
    def signUP(self,name,email,password):
        if len(password) > 8:
            return("Password should not be greater than 8 characters.")
        else:
            self.password = password
        return("User signed up successfully!")
name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
new_customer = User(username,email,password)
print(new_customer.sign_up)
         
     