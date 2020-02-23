"""***************************  TITLE  ****************************"""
"""912  Best Meeting Point.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
"""



"""***************************  EXAMPLES  ****************************"""
"""
0
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def minTotalDistance(self, grid):
        if not grid or not grid[0]:
            return 0
        
        def get_min_distance_1d(indices):
            left, right = 0, len(indices)-1
            res = 0
            while left < right:
                res += indices[right] - indices[left]
                left += 1
                right -= 1
                
            return res
        
        rows, cols = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
                    
        rows.sort()
        cols.sort()
        
        return get_min_distance_1d(rows) + get_min_distance_1d(cols)
        

