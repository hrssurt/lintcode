"""***************************  TITLE  ****************************"""
"""149  Best Time to Buy and Sell Stock.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Say you have an array for which the ith element is the price of a given stock on day i.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: [3, 2, 3, 1, 2]
Output: 1
Explanation: You can buy at the third day and then sell it at the 4th day. The profit is 2 - 1 = 1

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        min_price_so_far = float('inf')
        best_profit = 0
        for idx, price in enumerate(prices):
            if idx >= 1:
                best_profit = max(best_profit, price - min_price_so_far)
            min_price_so_far = min(min_price_so_far, price)
            
        return best_profit
            

