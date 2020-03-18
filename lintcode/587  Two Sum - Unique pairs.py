"""***************************  TITLE  ****************************"""
"""587  Two Sum - Unique pairs.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.
"""



"""***************************  EXAMPLES  ****************************"""
"""
unique pairs
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums or len(nums) <= 1:
            return 0
        nums.sort()
        start, end = 0, len(nums) - 1
        pairs = set()
        while start < end:
            if nums[start] + nums[end] == target:
                pairs.add((nums[start], nums[end]))
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1
        return len(pairs)
                
            

