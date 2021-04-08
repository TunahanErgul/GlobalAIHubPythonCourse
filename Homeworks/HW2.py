#login system with dictionary usage

accounts = {"admin":"administrator","ömer":"1234","tunahan":"12345"}

print("Welcome to Internet Banking \n")
print("To proceed, please enter your username and password correctly")

username = input("Enter your username: \n")
password = input("Enter your password: \n")


if username in  accounts and accounts[username]==password:
    print("You have succesfully entered to your account") 
else:
    print("You have  entered wrong username and password. \n ")
    print("Please try again later")
        
        
