"""***************************  TITLE  ****************************"""
"""200. Number of Islands.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1


Example 2:

Input:
11000
11000
00100
00011

Output: 3

"""



"""***************************  CODE  ****************************"""
class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        DX, DY = [0,1,0,-1], [-1, 0, 1, 0]
        
        def is_valid(grid, x, y, visited):
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and (x,y) not in visited and grid[x][y] == "1"
        
        def bfs(grid, x, y, visited):
            q = []
            count = 0
            if is_valid(grid, x, y, visited):
                q.append((x,y))
                count = 1           
            
            while q:
                x, y = q.pop()
                for dx, dy in zip(DX, DY):
                    nx, ny = x + dx, y + dy
                    if is_valid(grid, nx, ny, visited):
                        visited.add((nx, ny))
                        q.append((nx, ny))
            return count
            
            
        
        visited = set()
        s = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    s += bfs(grid, i, j, visited)
            
        return s
        
        
​
