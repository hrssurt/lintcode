"""***************************  TITLE  ****************************"""
"""151  Best Time to Buy and Sell Stock III.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Say you have an array for which the ith element is the price of a given stock on day i.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input : [4,4,6,1,1,4,2,5]
Output : 6

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices:
            return 0
        h1,h2,s1,s2 = float('-inf'), float('-inf'), 0, 0
        for price in prices:
            h1,s1,h2,s2 = max(h1, -price), max(s1, price+h1), max(h2, s1-price), max(s2, price+h2)
            
        return s2
