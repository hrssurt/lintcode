def soln(grid):
    DX, DY = [1,0,-1,0], [0,1,0,-1]
    if not grid or not grid[0]:
        return 0

    def is_valid(x, y, grid):
        return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] == 0

    q = []
    hours = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                q.append((i,j))

    zombie_count = len(q) 
    while q and zombie_count < len(grid) * len(grid[0]):
        size = len(q)
        for _ in range(size):
            x, y = q.pop(0)
            for dx, dy in zip(DX, DY):
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, grid):
                    q.append((nx, ny))
                    grid[nx][ny] = 1
                    zombie_count += 1
        
        hours += 1

    return hours

if __name__ == '__main__':
    # some test cases
    grid = [[1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]]
    print(soln(grid))


    grid = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1]]
    print(soln(grid))

    grid = [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]
    print(soln(grid))

    grid = [[0,1,0,0]]
    print(soln(grid))

