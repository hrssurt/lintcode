 # Note that input contians strings, not integers. "1" not 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        
        lands = self.find_all_lands(grid)
        visited = set()
        count = 0
        while lands:
            x, y = lands.pop()
            visited.add((x,y))
            self.bfs(grid, x, y, lands, visited)
            count += 1
            
        return count
    
    def is_valid(self, grid, x, y, visited):
        return x >= 0  and x < len(grid) and y  >= 0 and y < len(grid[0]) and grid[x][y] == "1" and (x,y) not in visited
    
    def find_all_lands(self, grid):
        s = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    s.add((i,j))
        return s
    
    def bfs(self, grid, x, y, lands, visited):
        q = [(x,y)]
        DX, DY = [0,1,0,-1], [1,0,-1,0]
        while q:
            x, y = q.pop(0)
            for dx, dy in zip(DX, DY):
                nx, ny = x+ dx, y + dy
                if self.is_valid(grid, nx, ny, visited):
                    visited.add((nx, ny))
                    q.append((nx, ny))
                    lands.remove((nx, ny))