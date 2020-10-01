username = ("admin")
password = ("12345password")
ug = ("")
pg = ("")
if input("Enter user ") == username:
    if input("Enter password") == password:
        print ("Access granted")
    else:
        print ("invalid password")
else:
    print("invalid user")
