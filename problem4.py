#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
import math
userip1 = input("Enter number 1 ")
userip2 = input("Enter number 2 ")
userip3 = input("Enter number 3 ")
n1 = int(userip1)
n2 = int(userip2)
n3 = int(userip3)
if n1 < n2 and n1 < n3:
    a = n1
    if n2 < n3:
        b = n2
        c = n3
    else:
        b = n3
        c = n2
elif n2 < n1 and n2 < n3:
    a = n2
    if n1 < n3:
        b = n1
        c = n3
    else:
        b = n3
        c = n1
else:
    a = n3
    if n2 < n1:
        b = n2
        c = n1
    else:
        b = n1
        c = n2
if (a * a + b * b)==(c*c):
    print ("that is a right triangle")
elif (a * a + b * b)>(c*c):
    print ("that is an acute triangle")
else:
    print ("that is an obtuse triangle")
