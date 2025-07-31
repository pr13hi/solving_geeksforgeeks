# Concept name : Number Problems

# Question : LCM And GCD

#            Given two integers a and b, You have to compute their LCM and GCD and return an array containing their LCM and GCD.
            
#                     Examples:
                    
#                     Input: a = 5 , b = 10
#                     Output: [10, 5]
#                     Explanation: LCM of 5 and 10 is 10, while their GCD is 5.
                      
# Solution : 

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        oa=a
        ob=b
        while a%b!=0:
            rem=a%b
            a=b
            b=rem
        gcd=b
        lcm=(oa*ob)//gcd
        return [lcm, gcd]

# Explanation : Preserve original values:
#                     Store a and b in oa and ob for later use in LCM calculation.
#               Compute GCD using the Euclidean algorithm:
#                     Repeatedly perform a % b and update a and b:
#                           while a % b != 0:
#                               rem = a % b
#                               a = b
#                               b = rem
#               Once the remainder is zero, b holds the GCD.
#               Calculate LCM using the formula:
#                     LCM = (original_a * original_b) // GCD
#               Return [LCM, GCD]
