"""***************************  TITLE  ****************************"""
"""150  Best Time to Buy and Sell Stock II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array prices, which represents the price of a stock in each day.
"""



"""***************************  EXAMPLES  ****************************"""
"""
prices
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                profit += prices[i] - prices[i-1]
                
        return profit
        
        
        

