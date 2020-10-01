username = ("admin")
password = ("12345password")
ug = ("")
pg = ("")
if input("Enter user ").strip() == username:
    if input("Enter password").strip() == password:
        print ("Access granted")
    else:
        print ("invalid password")
else:
    print("invalid user")
