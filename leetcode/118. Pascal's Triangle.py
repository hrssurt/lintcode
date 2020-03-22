"""***************************  TITLE  ****************************"""
"""118. Pascal's Triangle.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


"""



"""***************************  CODE  ****************************"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows: return []
        res = [[1]]
        for i in range(1, numRows):
            row = [1]
            prev_row = res[i-1]
            for j in range(1, i):     # with length i
                row.append(prev_row[j-1] + prev_row[j])
            
            row.append(1)
            res.append(row)
        
        return res
        
        
​
