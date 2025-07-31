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

def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
n,k=map(int,input().split())
arr=list(map(int,input().split()))[:n]
k=k%n
reverse(arr,0,n-1)
reverse(arr,0,k-1)
reverse(arr,k,n-1)
for i in arr:
    print(i,end=" ")

# Explanation : To rotate an array counter-clockwise by d elements, use the Reversal Algorithm:
#                           Reverse the first d elements.
#                           Reverse the remaining n - d elements.
#                           Reverse the entire array.
#               This efficiently rotates the array in-place using no extra space.
