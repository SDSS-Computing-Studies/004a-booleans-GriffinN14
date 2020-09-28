#! python3

# Have the user enter in a sentence. 
# Check to see if the word "password" is located in the sentence

# Inputs:
# a sentence

# Outputs:
# "the sentence contains password"
# "the sentence does not contain password"
userip = input("Enter sentace with \"password\" or not with ")
if ("password") in userip:
    print ("the sentence contains password")
else:
    print ("the sentence does not contain password")
