password="adminlog"
username= "system admin"
password_guess=0
password_limit=3

while password_guess < password_limit:
    name_guess = input("Enter the username: ")
    guess = input("Enter the password: ")
    password_guess += 1
    if guess == password and name_guess== username:
        print("Access Granted")
        break
    
else:
    print("ACCESS DENIED!")
    print("You have been locked out of the system, security measures have been deployed.")
    print("Survive, if you can.")