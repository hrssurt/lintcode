"""***************************  TITLE  ****************************"""
"""598  Zombie in Matrix.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.
"""



"""***************************  EXAMPLES  ****************************"""
"""
2
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        if not grid or not grid[0]:
            return -1
        W, Z, P = 2, 1, 0
        DX, DY = [0,1,0,-1], [1, 0, -1, 0]
        def is_valid(x, y, grid):
            return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] == P
        
        
        # use bfs
        q, day = [], 0
        alive = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == Z:
                    q.append((i,j))
                if grid[i][j] == P:
                    alive.add((i,j))
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.pop(0)
                for dx, dy in zip(DX, DY):
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny, grid):
                        grid[nx][ny] = Z
                        q.append((nx, ny))
                        alive.remove((nx, ny))
            day += 1
            if not alive:
                return day
        return -1
                
        
