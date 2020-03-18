"""***************************  TITLE  ****************************"""
"""1691  Best Time to Buy and Sell Stock V.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
heap:
"""



"""***************************  EXAMPLES  ****************************"""
"""
class Solution:
    """
    @param a: the array a
    @return: return the maximum profit
    """
    def getAns(self, a):
        # write your code here
        import heapq
        heap = [a[0]]
        profit = 0
        for num in a[1:]:
            if num > heap[0]:
                profit += num - heapq.heappop(heap)
                heapq.heappush(heap, num)
            heapq.heappush(heap, num)
        return profit

"""



"""***************************  CODE  ****************************"""
import heapq
class Solution:
    def getAns(self, a):
        profit = 0
        if not a:
            return profit
        heap = [a[0]]
        for price in a[1:]:
            if price > heap[0]:
                profit += price - heapq.heappop(heap)
                heapq.heappush(heap, price)
                
            heapq.heappush(heap, price)
            
        return profit

