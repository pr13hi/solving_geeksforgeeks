# Concept name : Number Problems

# Question : Odd Game

#            Given an array of length N, starting from 1 to N. At each iteration, you remove all elements at odd positions, until only one element is left. 
#            Find the last remaining element.
          
#                   Example 1:
                  
#                   Input:
#                   N = 5
#                   Output:
#                   4
#                   Explanation:
#                   Initial Array- {1,2,3,4,5}.
#                   After 1st Iteration- {2,4}.
#                   After 2nd Interation- {4}
#                   Threfore, the answer is 4.
                      
# Solution : 

class Solution:
    def oddGame(self, N):
        power=1
        while power*2<=N:
            power*=2
        return power

# Explanation : Iterate to find the largest power of 2 ≤ N:
#               Initialize power = 1 as the smallest power of 2.
#               While doubling power doesn't exceed N, keep updating power *= 2.
#         Why this works:
#               At each elimination round, you remove elements at odd positions.
#               This pattern keeps halving the list, and only the elements at indices that are powers of 2 survive longer.
#               Eventually, only the largest such element remains.
#         Return the last power found. This is the final surviving number in the game.
