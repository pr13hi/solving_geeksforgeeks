# Question : Check the status

            # Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.
            # Return True for the following cases:
                    # Either a or b (not both) is non-negative and the flag is false.
                    # Both a and b are negative and the flag is true.
            # Otherwise, return False.

# Solution :

class Solution:
    def checkStatus(self, a, b, flag):
        if flag:
            return a < 0 and b < 0
        else:
            return (a < 0 <= b) or (b < 0 <= a)


