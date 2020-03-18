""" Description
"""
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
"""

"""Example
"""

"""Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

""" Code
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left_max, right_max = [], []
        cur_max = float('-inf')
        for n in height:
            cur_max = max(n, cur_max)
            left_max.append(cur_max)
        cur_max = float('-inf')    
        for n in reversed(height):
            cur_max = max(cur_max, n)
            right_max.insert(0, cur_max)
            
        
        s = 0
        for i, n in enumerate(height):
            if min(left_max[i], right_max[i]) > n:
                s += min(left_max[i], right_max[i]) - n
                
        return s
        