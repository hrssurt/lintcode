"""***************************  TITLE  ****************************"""
"""1811  Find  Maximum Gold.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
M*N grid, each grid has a number representing the number of golds in that grid. 0 if it is empty. Find a path to get the maximum sum of golds under conditions: 1. 1. A road can't walk a repeating grid 2. Never cross a zero.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example:
Input:
grid = [[1,2,0,0],
       [0,0,2,2]]
Output: 4

"""



"""***************************  CODE  ****************************"""
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and                 grid[x][y] != 0
        
        visited = set()
        def dfs(x, y, grid):
            max_gold = grid[x][y]
            new = float('-inf')
            for dx, dy in zip(DX, DY):
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new = max(new, dfs(nx, ny, grid))
                    visited.remove((nx, ny))
            
            if new == float("-inf"):
                return max_gold
            else:
                return max_gold + new
            
        max_reward = float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                visited.add((i,j))
                r = dfs(i, j, grid)
                visited.remove((i,j))
                max_reward = max(max_reward, r)
        return max_reward
                
