"""***************************  TITLE  ****************************"""
"""897  Island City.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a matrix of size n x m, the elements in the matrix are 0、1、2. 0 for the sea, 1 for the island, and 2 for the city on the island(You can assume that 2 is built on 1, ie 2 also represents the island).
If two 1 are adjacent, then these two 1 belong to the same island. Find the number of islands with at least one city.
"""



"""***************************  EXAMPLES  ****************************"""
"""
n x m
"""



"""***************************  CODE  ****************************"""


class Solution:
    def numIslandCities(self, grid):
        if not grid or not grid[0]:
            return 0
            
        DX, DY = [1,0,-1,0], [0,1,0,-1]
        
        def is_valid(grid, x, y, visited):
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and (x, y) not in visited and grid[x][y] != 0
            
        def bfs(grid, x, y, visited):
            visited.add((x, y))
            q = [(x,y)]
            city_found = False if grid[x][y] == 1 else True
            while q:
                x, y = q.pop(0)
                for dx, dy in zip(DX, DY):
                    nx, ny = x + dx, y + dy
                    if is_valid(grid, nx, ny, visited):
                        visited.add((nx, ny))
                        q.append((nx, ny))
                        if grid[nx][ny] == 2:
                            city_found = True
            return city_found
                
        count = 0
        q = []
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 or grid[i][j] == 2 and (i, j) not in visited:
                    result = bfs(grid, i, j, visited)
                    if result:
                        count += 1
                        
        return count
