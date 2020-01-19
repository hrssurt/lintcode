"""***************************  TITLE  ****************************"""
"""1802  Grid Game.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a grid with n rows and m columns of binary integers, 0 or 1, and a set of rules, simulate k turns of the game on this grid.The given grid denotes the initial configuration for the game, where grid[i][j] = 1 denotes that cell in the ith row and jth column is alive, and grid[i][j] = 0 denotes that this cell is dead. Two cells are neighbors when they share at least one common corner, thus each cell has at most 8 neighbors, as shown in the picture below:
There is a list of 9 rules indexed from 0 to 8, each rule having a value of either "alive" or "dead".A single rule,i,specifies what happens to the cells with exactly i alive neighbors.In each turn the new value of a cell  is determined by counting the number of "alive" neighbors and applying the rule at index corresponding to the count. The value corresponding to the rule is used to set new value in the cell
The "Live neughbors for each cell" grid at turn 1 contains the number of adjoining live cells at each grid position for turn 0.It is used to create the new grid state for turn 1. At each cell with a value of 3 or 5, the related cell in the new grid is set to alive. All of the others are set to dead, The resultant grid is similarly analyzed for the second turn. The returned 2-dimensional array contains the grid rows shown at turn 2 above.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example:
input:
grid: [[0, 1, 1, 0], [1, 1, 0, 0]]
rules: ["dead", "dead", "dead", "alive", "dead", "alive", "dead", "dead", "dead"]
turn: 2
output:[[0, 1, 1, 0], [1, 1, 0, 0]]
Explanation：
turn 1:
because live neighbors grid:
[[3, 3, 2, 1],
 [2, 3, 3, 1]]
3 and 5 are alive, thus turn 1 grid is:
[[1, 1, 0, 0],
 [0, 1, 1, 0]]

turn 2:
live neighbors grid:
[[2, 3, 3, 1],
 [3, 3, 2, 1]]
thus turn 2 grid is
[[0, 1, 1, 0],
 [1, 1, 0, 0]]

"""



"""***************************  CODE  ****************************"""
import copy

class Solution:
    def GridGame(self, grid, rules, k):
        if not grid or not grid[0]:
            return grid
        DX = [0, 0, -1, 1, 1, -1, 1, -1]
        DY = [1, -1, 0, 0, 1, -1, -1, 1]
        status_map = {"alive": 1, "dead": 0}
        def count_live_neighbours(x, y, grid):
            count = 0
            for dx, dy in zip(DX, DY):
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                    count += grid[nx][ny]
            return count
        
        while k:
            new_grid = copy.deepcopy(grid)
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    count = count_live_neighbours(i, j, grid)
                    status = status_map[rules[count]]
                    new_grid[i][j] = status
            k -= 1
            grid = new_grid
        return new_grid
