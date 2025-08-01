# Concept name : Number Problem

# Question : Sum of Digit is Palindrome or not

#            Given a number n. Return true if the digit sum(or sum of digits) of n is a Palindrome number otherwise false.
#            A Palindrome number is a number that stays the same when reversed
          
#                   Examples:
                  
#                   Input: n = 56
#                   Output: true
#                   Explanation: The digit sum of 56 is 5+6 = 11. Since, 11 is a palindrome number.Thus, answer is true.

# Solution : 

class Solution:
    def isDigitSumPalindrome(self, n):
        sum=0
        for i in str(n):
            sum+=int(i)
        s=str(sum)
        if s==(s[::-1]):
            return True
        else:
            return False
      
