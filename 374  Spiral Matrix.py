"""***************************  TITLE  ****************************"""
"""374  Spiral Matrix.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:	[[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]
Output: [1,2,3,6,9,8,7,4,5]

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        res, x, y, n, m = [], 0, 0, len(matrix), len(matrix[0])
        DX, DY = [0, 1, 0, -1], [1, 0, -1, 0]
        while len(res) < n * m:
            
            # for each direction
            for dx, dy in zip(DX, DY):
                while True:             # loop to fill this direction
                    if matrix[x][y]:
                        res.append(matrix[x][y])
                        matrix[x][y] = None
                    x, y = x + dx, y + dy
                    if not self.is_valid(matrix, x, y, n, m):
                        x, y = x - dx, y - dy
                        break
            y += 1   # move on to the inner loop

            
        return res
                    
    def is_valid(self, matrix, x, y, n, m):
        return x >= 0 and y >= 0 and x < n and y < m and matrix[x][y] is not None
    
        

