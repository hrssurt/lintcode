"""
Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.
"""

"""
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
"""

from heapq import heappush, heappop
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        def is_valid(grid, x, y, visited):
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and (x,y) not in visited
        
        DX, DY = [0,1,0,-1], [1,0,-1,0]
        
        m, n = len(heightMap), len(heightMap[0])
        q = []
        visited = set()
        
        # adding the surrounding to the q
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1  or j == 0 or j == n-1 and (i, j) not in visited:
                    t = (heightMap[i][j], i, j)
                    heappush(q, t)
                    visited.add((i,j))
        
        waterlevel, cur_water = 0, 0

        while q:
            h, x, y = heappop(q)
            waterlevel = max(waterlevel, h)
                
            for dx, dy in zip(DX, DY):
                nx, ny = x + dx, y + dy
                if is_valid(heightMap, nx, ny, visited):
                    heappush(q, (heightMap[nx][ny], nx, ny))
                    if waterlevel > heightMap[nx][ny]:
                        cur_water += waterlevel - heightMap[nx][ny] 
                visited.add((nx,ny))
                    
        return cur_water
                
            
        
                    
                    
                    
        
                    
    
                    
        
        