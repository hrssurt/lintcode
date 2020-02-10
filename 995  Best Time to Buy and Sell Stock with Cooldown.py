"""***************************  TITLE  ****************************"""
"""995  Best Time to Buy and Sell Stock with Cooldown.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Say you have an array for which the ith element is the price of a given stock on day i.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: [1, 2, 3, 0, 2]
Output: 3
Explanation:
transactions = [buy, sell, cooldown, buy, sell]

"""



"""***************************  CODE  ****************************"""
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        buy = [0 for _ in prices]
        sell = [0 for _ in prices]
        buy[0] = -prices[0]
        
        for i in range(1, len(prices)):
            if i >= 2:
                buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            else:
                buy[i] = max(-prices[i], buy[i-1])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        return sell[-1]
