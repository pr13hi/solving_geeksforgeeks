# Question : Intro to Dictionary
#            The task is to complete the function create_dict() which takes arr as input and creates a dictionary then returns it.

# Solution :

def create_dict(arr):
    dict = {}
    for name,marks in arr:
        dict[name]=marks
    return dict
