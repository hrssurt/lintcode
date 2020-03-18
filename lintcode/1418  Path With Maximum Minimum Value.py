"""***************************  TITLE  ****************************"""
"""1418  Path With Maximum Minimum Value.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example1:
Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 

"""



"""***************************  CODE  ****************************"""
import heapq

class Solution:
    def maximumMinimumPath(self, A):
        DX, DY = [1,0,-1,0], [0,1,0,-1]
        visited = set()
        q = []
        def is_valid(x, y, visited):
            return x >= 0 and y >= 0 and x < len(A) and y < len(A[0]) \
                and (x,y) not in visited
        
        min_val = float('inf')
        visited.add((0,0))
        heapq.heappush(q, (-A[0][0], 0, 0))
        while q:
            cur_num, x, y = heapq.heappop(q)
            min_val = min(min_val, -cur_num)
            if x == len(A) -1 and y == len(A[0]) -1:
                return min_val
            
            for dx, dy in zip(DX, DY):
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, visited):
                    heapq.heappush(q, (-A[nx][ny], nx, ny))
                    visited.add((nx, ny))
                    
               
        return -1
            
