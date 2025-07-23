# Question : Move All Zeroes to End

#            You are given an array arr[] of non-negative integers. 
#            Your task is to move all the zeros in the array to the right end while maintaining the relative order of the non-zero elements. 
#            The operation must be performed in place, meaning you should not use extra space for another array.
            
#                           Examples:
                          
#                           Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
#                           Output: [1, 2, 4, 3, 5, 0, 0, 0]
#                           Explanation: There are three 0s that are moved to the end.

# Solution :

class Solution:
	def pushZerosToEnd(self,arr):
    	i=0
    	for j in range(len(arr)):
    	    if arr[j]!=0:
    	        arr[i],arr[j]=arr[j],arr[i]
    	        i+=1

# Explanation : Use two pointers:
#                             j to scan through the entire list,
#                             i to track the position where the next non-zero element should be placed.
#               Whenever find a non-zero element at arr[j], swap it with arr[i] and increment i.
#               This way, all non-zero elements are moved to the front, and the zeros shift toward the end — all in one pass and in-place.
