"""***************************  TITLE  ****************************"""
"""1000  Best Time to Buy and Sell Stock with Transaction Fee.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee. (You need to pay fee only on selling.)
"""



"""***************************  EXAMPLES  ****************************"""
"""
fee
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def maxProfit(self, prices, fee):
        if not prices:
            return 0
            
        hold = [0 for _ in range(len(prices))]
        unhold = [0 for _ in range(len(prices))]
        
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            hold[i] = max(hold[i-1], unhold[i-1] - prices[i])
            unhold[i] = max(unhold[i-1], hold[i-1] + prices[i] - fee)
            
        return unhold[-1]

