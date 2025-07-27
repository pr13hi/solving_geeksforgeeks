# Concept name : Array

# Question : Majority Element - More Than n/3

#            Given an array arr[] consisting of n integers, the task is to find all the array elements which occurs more than floor(n/3) times.
#            Note: The returned array of majority elements should be sorted.
          
#                     Examples:
                    
#                     Input: arr[] = [2, 2, 3, 1, 3, 2, 1, 1]
#                     Output: [1, 2]
#                     Explanation: The frequency of 1 and 2 is 3, which is more than floor n/3 (8/3 = 2).

# Solution : 

class Solution:
    def findMajority(self, arr):
        n=len(arr)
        freq={}
        l=[]
        for i in arr:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for keys,count in freq.items():
            if count>n/3:
                l.append(keys)
        l.sort()
        return l
    
# Explanation : Create an empty dictionary freq to store frequencies of each number.
#               Traverse the array:
#                         If a number is not in the dictionary, initialize it with 1.
#                         Else, increment its count.
#               After the count is complete, loop through freq.items():
#                         If the count of an element is greater than n // 3, add it to the result list l.
#               Sort the result list l before returning.
