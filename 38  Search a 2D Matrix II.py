"""***************************  TITLE  ****************************"""
"""38  Search a 2D Matrix II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:
	[[3,4]]
	target=3
Output:1

"""



"""***************************  CODE  ****************************"""
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix)-1, len(matrix[0])-1
        i, j = m, 0
        greater_or_equal, less_or_equal = 0, 0
        while i >= 0 and j <= n:
            if matrix[i][j] <= target:
                less_or_equal += i+1
                j += 1
            else:
                i -= 1
                
        i, j = 0, n
        while i <= m and j >= 0:
            if matrix[i][j] >= target:
                greater_or_equal += m-i+1
                j -= 1
            else:
                i+=1
                
        return greater_or_equal + less_or_equal - (m+1) * (n+1)
            
        
        
