# Question : Dictionary in Python - II

#            Given a list arr[], of positive integers, and an integer sum. The task is to check if any pair exists in the array whose sum is equal to the given sum. 
#            If such a pair exists return true, otherwise, return false.

#                       Example:
                      
#                       Input: arr[] = [1, 2, 3, 3, 5], sum = 8 
#                       Output: true
#                       Explanation: Pair with sum 8 is present in the array which is (3, 5).

# Solution : 

def pair_sum(dict, arr, sum):
    for i in arr:
        j=sum-i
        if j in dict:
            if j==i:
                if dict.get(i)>1:
                    return True
            else:
                return True
    return False

# Explanation : Loop through each element i in the array.
#               Compute the complement j = sum - i.
#               Check if j exists in the dictionary:
#                     If i == j, make sure there are at least 2 occurrences of i in the dictionary.
#                     If i != j, just check if j is present.
#               If any valid pair is found, return True. Otherwise, return False.
