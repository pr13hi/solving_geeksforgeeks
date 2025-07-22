# Question : Test if tuple is distinct
#            Given a tuple arr , print "True" if all elements of tuple are different otherwise print "False".

# Solution :

arr = tuple(map(int, input().split()))
new=set(arr)
if len(arr)==len(new):
    print("True")
else:
    print("False")
