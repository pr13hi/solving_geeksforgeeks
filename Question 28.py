# Concept name : Array

# Question : Next Permutation

#            Given an array of integers arr[] representing a permutation, 
#            implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. 
#            If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 
#            Note:  A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order.
          
#                     Examples:
                    
#                     Input: arr[] = [2, 4, 1, 7, 5, 0]
#                     Output: [2, 4, 5, 0, 1, 7]
#                     Explanation: The next permutation of the given array is [2, 4, 5, 0, 1, 7].

# Solution : 

class Solution:
    def nextPermutation(self, arr):
        i=len(arr)-2
        while(i>=0 and arr[i]>=arr[i+1]):
            i-=1
        if(i>=0):
            j=len(arr)-1
            while(j>=0 and arr[j]<=arr[i]):
                j-=1
            arr[i],arr[j]=arr[j],arr[i]
        arr[i+1:]=sorted(arr[i+1:])
    
# Explanation : Find the first decreasing element from the end (pivot):
#                     Traverse the array from right to left, find the first index i such that arr[i] < arr[i+1].
#                     If no such index exists, the permutation is the last one (i.e., descending). Reverse the array to get the first permutation.
#               Find the element just larger than arr[i] to the right of it:
#                     Traverse again from the right and find the first index j such that arr[j] > arr[i].
#               Swap arr[i] and arr[j]:
#                     This ensures the next greater number is formed.
#               Reverse the subarray to the right of i:
#                     Since the suffix is in decreasing order, reversing it will make it the smallest possible (i.e., next permutation).
