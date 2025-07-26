# Question : Dictionary in Python - III

#            Given a list of some students in a list and their corresponding marks in another list. The task is to do some operations as described below:
#                a. i key value: Iserts key and value in the dictionary, and print 'Inserted'.
#                b. d key: Delete the entry for a given key and print 'Deleted' if the key to be deleted is present, else print '-1'.
#                c. key: Print marks of a given key in a statement as "Marks of student name is : marks".

# Solution :

def insert_dict(query, dict):
     dict.update({query[1]:query[2]})
   
def del_dict(query, dict):
     if query[1] in dict.keys():
        del dict[query[1]]

def print_dict(key, dict):
     if key in dict.keys():
        print("Marks of %s is %s" %(key,dict[key])) 
     else:
        return False
    
    
