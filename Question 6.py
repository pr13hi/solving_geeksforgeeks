# Question : Jumping through While

#            Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).

# Solution :

def printIncreasingPower(x):
    i=1
    j=1
    while(j<x):
        j=i
        i+=1
        j*=j
        if j<=x:
            print (j , end = " ")
