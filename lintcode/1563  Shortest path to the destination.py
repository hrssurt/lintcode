"""***************************  TITLE  ****************************"""
"""1563  Shortest path to the destination.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a 2D array representing the coordinates on the map, there are only values 0, 1, 2 on the map. value 0 means that it can pass, value 1 means not passable, value 2 means target place. Starting from the coordinates [0,0],You can only go up, down, left and right. Find the shortest path that can reach the destination, and return the length of the path.
"""



"""***************************  EXAMPLES  ****************************"""
"""
0, 1, 2
"""



"""***************************  CODE  ****************************"""
    def shortestPath(self, targetMap):
        visited = set()
        DX = [1, 0, -1, 0]
        DY = [0, 1, 0, -1]
        def is_valid(x, y, grid):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 1
        
        def dfs(x, y, grid):
            if grid[x][y] == 2:
                return 0
            
            min_dis = float('inf')    
            for dx, dy in zip(DX, DY):
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    min_dis = min(min_dis, 1 + dfs(nx, ny, grid))
                    visited.remove((nx, ny))
            return min_dis
            
        if not targetMap or not targetMap[0]:
            return 0
        visited.add((0,0))    
        d = dfs(0, 0, targetMap)
        if d == float("inf"):
            return -1
        else:
            return d
