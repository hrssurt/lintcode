"""***************************  TITLE  ****************************"""
"""117  Jump Game II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""

Given an array of non-negative integers, you are initially positioned at the first index of the array.

"""



"""***************************  EXAMPLES  ****************************"""
"""
Input : [2,3,1,1,4]
Output : 2
Explanation : The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        if not A or len(A) <= 1:
            return 0
        step = cur_max = next_max = idx = 0
        
        while idx <= cur_max:
            while idx <= cur_max:
                next_max = max(A[idx] + idx, next_max)
                idx += 1
            step += 1
            if next_max >= len(A)-1:
                return step
                
            cur_max = next_max
                
        return 0
        

