# Question : Regex

#            This is a function problem. Do not take any input. just Complete the function numberMatcher() that takes str as input and print numbers in it, 
#            If there are no numbers then print -1.

# Solution :

import re
def numberMatcher(str):
    pat="[0-9]+"
    match=re.findall(pat,str) 
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")
