# Question : Second Largest

#            Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
#            Note: The second largest element should not be equal to the largest element.

#                     Examples:
                    
#                     Input: arr[] = [12, 35, 1, 10, 34, 1]
#                     Output: 34
#                     Explanation: The largest element of the array is 35 and the second largest element is 34.

# Solution :

class Solution:
    def getSecondLargest(self, arr):
        unique=list(set(arr))
        if len(unique)<2:
            return -1
        unique.sort()
        return unique[-2]

# Explanation : First convert the list to a set to remove duplicates, since we're only interested in distinct elements.
#               Then, check if the set has at least two unique elements — if not, return -1 as there is no second largest.
#               If it does, sort the list and return the second last element (-2 index), which is the second largest number.
