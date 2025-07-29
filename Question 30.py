# Concept name : Array

# Question : Stock Buy and Sell – Max one Transaction Allowed

#            Given an array prices[] of length n, representing the prices of the stocks on different days. 
#            The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. 
#            Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.
#            Note: Stock must be bought before being sold.
          
#                       Examples:
                      
#                       Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
#                       Output: 8
#                       Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.
                      
# Solution : 

class Solution:
    def maximumProfit(self, prices):
        mini=prices[0]
        profit=0
        for i in range(1,len(prices)):
            cost=prices[i]-mini
            profit=max(profit,cost)
            mini=min(mini,prices[i])
        return profit

# Explanation : Initialize mini = prices[0] to keep track of the lowest price so far (best day to buy).
#               Initialize profit = 0 to store the maximum profit seen so far.
#               Loop through the array from index 1 to len(prices) - 1:
#                         Calculate the cost = prices[i] - mini, which is the profit if we bought at mini and sold at prices[i].
#                         Update profit = max(profit, cost) — keep the maximum profit seen so far.
#                         Update mini = min(mini, prices[i]) — always track the lowest price to buy in the past.
#               After the loop, return profit.
