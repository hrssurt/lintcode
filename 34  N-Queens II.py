"""***************************  TITLE  ****************************"""
"""34  N-Queens II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Follow up for N-Queens problem.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: n=1
Output: 1
Explanation:
1:
1

"""



"""***************************  CODE  ****************************"""
class Solution:
    def totalNQueens(self, n):
        self.res = 0
        if n <= 0:
            return self.res
            
        self.dfs([], 0, n)
        return self.res
    def dfs(self, usedCols, curRow, n):
        if curRow == n:
            self.res += 1
            
        for curCol in range(n):
            if self.is_valid(usedCols, curRow, curCol):
                usedCols.append(curCol)
                self.dfs(usedCols, curRow + 1, n)
                usedCols.pop(-1)
                
    def is_valid(self, usedCols, curRow, curCol):
        for usedRow, usedCol in enumerate(usedCols):
            if curCol == usedCol or abs(curRow - usedRow) == abs(curCol - usedCol):
                return False
                
        return True
        
        

