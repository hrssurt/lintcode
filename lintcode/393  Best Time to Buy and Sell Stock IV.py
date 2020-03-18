"""***************************  TITLE  ****************************"""
"""393  Best Time to Buy and Sell Stock IV.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array prices and the i-th element of it represents the price of a stock on the i-th day.
"""



"""***************************  EXAMPLES  ****************************"""
"""
prices
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        if not K or not prices:
            return 0
        
        if K >= len(prices) // 2:
            # it is like unlimited transactions
            # just using greedy algorithm
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
            
        
        variables = [float("-inf") if idx % 2 == 0 else 0 for idx in range(K*2)]
        for price in prices:
            for idx, ki in enumerate(variables):
                if idx == 0:
                    variables[0] = max(ki, -price)
                elif idx % 2 == 0:      # the hold pbalances
                    variables[idx] = max(ki, variables[idx-1] - price)
                else:
                    variables[idx] = max(ki, variables[idx-1] + price)
                    


        return variables[-1]
                    

