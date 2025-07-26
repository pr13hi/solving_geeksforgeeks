# Question : Implement Set in Python

#            Given Q queries to do some operation on Set, the task is to perform all the queries in the Set as given below:
#                 a. i element: Adds element to the set.
#                 b. r element: Remove element from set.
#                 c. s: Find sum of elements in set. Returns the sum of elements in Set.

# Solution :

def insert(s, element):
    return s.add(element)

def remove_from_set(s, element):
    return s.discard(element)

def sum_set(s):
    return sum(s)
    
    
