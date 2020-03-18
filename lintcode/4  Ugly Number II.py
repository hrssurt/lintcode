"""***************************  TITLE  ****************************"""
"""4  Ugly Number II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Ugly number is a number that only have prime factors 2, 3 and 5.
"""



"""***************************  EXAMPLES  ****************************"""
"""
2
"""



"""***************************  CODE  ****************************"""
import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        # using bfs
        
        q = []
        count = 1
        q.append(1)
        
        visited =set()
        while q:
            p = heapq.heappop(q)
            if count == n:
                return p
            else:
                count += 1
                p1 = p *2
                p2 = p *3
                p3 = p *5
                for e in [p1, p2, p3]:
                    if e not in visited:
                        visited.add(e)
                        heapq.heappush(q, e)
