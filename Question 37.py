# Concept name : Array

# Question : Array Subset

#            Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

#               Examples:
              
#               Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
#               Output: true
#               Explanation: b[] is a subset of a[]

# Solution : 

class Solution:
    def isSubset(self, a, b):
        adic={}
        bdic={}
        
        for i in a:
            adic[i]=adic.get(i,0)+1
            
        for i in b:
            bdic[i]=bdic.get(i,0)+1
            
        for key in bdic:
            if bdic[key]>adic.get(key,0):
                return False
        return True
    
    
    
    
