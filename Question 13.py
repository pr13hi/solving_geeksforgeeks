# Question : Slicing in String
#            Given a string of braces named bound_by, and a string named tag_name. The task is to print a new string such that tag_name is in the middle of bound_by.

# Solution :

def join_middle(bound_by, tag_name):
  return bound_by[0:(len(bound_by)//2)] + tag_name + bound_by[(len(bound_by)//2):len(bound_by)]
