# Question : Set in Python - II

#            Given some elements in two sets a and b, the task is to find the elements common in two sets, elements in both the sets, 
#            elements that are only in set a, not in b.

# Solution :

def common_in_set(a, b):
    return a.intersection(b)

def diff(a, b):
    return a.difference(b)

def all_in_set(a, b):
    return a.union(b)
    
