#! python3
# Have the user input a number 
# Determine if the number is positive, negative or 0 
# 2 points

# Inputs:
# number

# Outputs:
# - "positive"
# - "negative"
# - "zero"
userip = input("Enter number ")
if float(userip) > 0:
    print ("positive")
elif float(userip) < 0:
    print("negative")
else:
    print("zero")
