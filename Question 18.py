# Question : String Functions - I
#            You'll be given a string str and x, you'll perform various operations on them.

# Solution :

def trim(str):
    return str.strip()

def exists(str, x):
    return str.find(x)

def titleIt(str):
    return str.title()

def casesSwap(str):
    return str.swapcase()
