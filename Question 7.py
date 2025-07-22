# Question : For loop
#            You are given a number N, you need to print its multiplication table.

# Solution :

def multiplicationTable(N):
    for i in range(1,11):
        print(N*i,end=" ")
