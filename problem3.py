 #! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks
username = ("admin")
password = ("12345password")
ug = ("")
pg = ("")
while not pg == password:
    ug = input("Enter username ").strip()
    if ug == username :
        pg = input("Enter password ").strip()
        if pg == password:
            break
        else:
            print ("invalid password")
    else:
        print ("invalid user")
print("Access granted")
