# Concept name : Array

# Question : Rotate Array

#            Given an array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. 
#            Do the mentioned change in the array in place.
#            Note: Consider the array as circular.
                      
#                       Examples :
                      
#                       Input: arr[] = [1, 2, 3, 4, 5], d = 2
#                       Output: [3, 4, 5, 1, 2]
#                       Explanation: when rotated by 2 elements, it becomes 3 4 5 1 2.

# Solution :

class Solution:
    def rotateArr(self, arr, d):
        n=len(arr)
        d%=n
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,n-1)
        self.reverse(arr,0,n-1)
        
    def reverse(self,arr,left,right):
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1

# Explanation : To rotate an array counter-clockwise by d elements, use the Reversal Algorithm:
#                           Reverse the first d elements.
#                           Reverse the remaining n - d elements.
#                           Reverse the entire array.
#               This efficiently rotates the array in-place using no extra space.
