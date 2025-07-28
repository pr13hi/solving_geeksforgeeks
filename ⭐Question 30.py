# Concept name : Searching

# Question : Binary Search

#            Given a sorted array arr[] and an integer k, find the position(0-based indexing) at which k is present in the array using binary search. 
#            If k doesn't exist in arr[] return -1. 
          
#            Note: If multiple occurrences are there, please return the smallest index.
          
#                     Examples:
                    
#                     Input: arr[] = [1, 2, 3, 4, 5], k = 4
#                     Output: 3
#                     Explanation: 4 appears at index 3.

# Solution : 

class Solution:
    def binarysearch(self, arr, k):
        n=len(arr)
        low=0
        high=n-1
        result=-1
        while low<=high:
            mid=int((low+high)/2)
            if arr[mid]==k:
                result=mid
                high=mid-1
            elif arr[mid]<k:
                low=mid+1
            else:
                high=mid-1
        return result
    
# Explanation : Initialize low = 0, high = n - 1, and result = -1.
#               While low <= high:
#                   Compute mid = (low + high) // 2
#                   If arr[mid] == k:
#                       Store mid in result as a possible answer.
#                       Move high = mid - 1 to search on the left side.
#                   Else if arr[mid] < k, move low = mid + 1.
#                   Else, move high = mid - 1.
#               After the loop, return result.
