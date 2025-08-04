# Concept name : Number Problem

   # Question : Odd or Even

   #            Given a number n, determine whether it is a prime number or not.
   #            Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
              
   #                      Examples :
                        
   #                      Input: n = 7
   #                      Output: true
   #                      Explanation: 7 has exactly two divisors: 1 and 7, making it a prime number.

# Solution : 

class Solution:
    def isPrime(self, n):
        if n<2:
            return False
        sqr=math.sqrt(n)
        for i in range(2,int(sqr)+1):
            if n%i==0:
                return False
        return True
