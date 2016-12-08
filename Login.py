import time
import PassManager

# Just the login function. Basic script to ask for login, after the login
# credentials are verified, then run the PassManager.py


print("Welcome to PassManager")
time.sleep(1)
# Variable to represent their login status, loop until they login
login_status = False
while(not login_status):
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    
    # Check the credentials
    if(username == "user1" and password == "pass1"):
        print("Welcome " + username)
        login_status = True
        print("PassManager is now launching...")
        


time.sleep(5)

passManager = PassManager.PassManager()