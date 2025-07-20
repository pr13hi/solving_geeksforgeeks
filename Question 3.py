# Question : If conditional statement
#             There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.
#             Now, complete the function which returns true if you are in trouble, else return false

# Solution :

class Solution:
    def checkStatus(self, a, b, flag):
        if flag:
            return a < 0 and b < 0
        else:
            return (a < 0 <= b) or (b < 0 <= a)
