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
userip3 = input("Enter number 3 make this number highr than the two before it ")
userip1 = float(userip1)
userip2 = float(userip2)
userip3 = float(userip3)
if (userip1 * userip1 + userip2 * userip2)==(userip3*userip3):
    print ("that is a right triangle")
elif (userip1 * userip1 + userip2 * userip2)>(userip3*userip3):
    print ("that is an acute triangle")
else:
    print ("that is an obtuse triangle")
