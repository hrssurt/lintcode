"""***************************  TITLE  ****************************"""
"""1536  Find First and Last Position of Element in Sorted Array.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
"""



"""***************************  EXAMPLES  ****************************"""
"""
nums
"""



"""***************************  CODE  ****************************"""
class Solution:
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        start, end = 0, len(nums)-1
        first, second = -1, -1    

        while start + 1 < end:
            mid = start + (end- start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        
        if nums[start] == target:
            first = start
        elif nums[end] == target:
            first = end
            
        # doing binary search the second time
        # this time, we are doing something different
        # we are moving the start to mid more often
        
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
                
        
        if nums[end] == target:
            second = end
        elif nums[start] == target:
            second = start
            
        return [first, second]
            
            
