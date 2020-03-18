"""***************************  TITLE  ****************************"""
"""1225  Island Perimeter.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
对于一片陆地，
"""



"""***************************  EXAMPLES  ****************************"""
"""
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16

"""



"""***************************  CODE  ****************************"""
class Solution:
    def islandPerimeter(self, grid):
        LAND = 1
        WATER = 0
        DX, DY = [1, 0, -1, 0], [0, 1, 0, -1]
        def count_p(x, y, grid):
            count = 0
            for dx, dy in zip(DX, DY):
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or \
                    grid[nx][ny] == WATER:
                    count += 1
            return count
                    
        if not grid or not grid[0]:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == LAND:
                    count += count_p(i, j, grid)
        return count
                    

