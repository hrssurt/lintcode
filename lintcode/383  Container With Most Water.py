"""***************************  TITLE  ****************************"""
"""383  Container With Most Water.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
"""



"""***************************  EXAMPLES  ****************************"""
"""
(i, ai)
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        if not heights or len(heights) <= 1:
            return 0
            
        left, right = 0, len(heights) -1
        max_area = 0
        while left < right:
            cur_area = min(heights[right], heights[left]) * (right -left)
            max_area = max(max_area, cur_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

