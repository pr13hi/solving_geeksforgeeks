# Question : Zero Converter

#            You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. 
#            If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.
#            Note:- You don't have to return anything, you just have to print the array.

# Solution :

def pos(n):
    if(n>0):
        for i in range(n-1,-1,-1):
            print(i,end=" ")
    if(n==0):
        print("already Zero")
        
    
def neg(n):
    if(n<0):
        for i in range(n,1):
            print(i,end=" ")
    if(n==0):
        print("already Zero")
        
