# Concept name : Number Problem

 # Question : Armstrong Numbers

 #            You are given a 3-digit number n, Find whether it is an Armstrong number or not.
 #            An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 
 #            371 is an Armstrong number since 33 + 73 + 13 = 371. 
            
 #                  Examples:
                  
 #                  Input: n = 153
 #                  Output: true
 #                  Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153. 

# Solution : 

class Solution:
    def armstrongNumber (self, n):
        temp=n
        sum_arm=0
        while temp>0:
            digit=temp%10
            sum_arm+=digit**3
            temp=temp//10
        if n==sum_arm:
            return True
        return False

# Explanation: Armstrong number of 3 digits → sum of cubes of its digits equals the number itself.
#               1. Extract each digit using modulo and integer division.
#               2. Cube each digit and add to sum.
#               3. If the sum equals the original number → it's an Armstrong number.
#               4. Return 1 if True, else 0.
