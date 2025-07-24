# Question : String Functions - II 
#            Given a string S, the task is to determine whether the string starts and ends with the characters 'gfg' (case insensitive)

# Solution :

def gfg(S):
    b = S.lower()
    if (b.startswith('gfg') or b.endswith('gfg')):
        print("Yes")
    else:
        print("No")
