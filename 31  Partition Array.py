"""***************************  TITLE  ****************************"""
"""31  Partition Array.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:
"""



"""***************************  EXAMPLES  ****************************"""
"""
nums
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums: return 0
        
        left, right = 0, len(nums) - 1
        while left <= right:
            while left < len(nums) and nums[left] < k:
                left += 1
                
            while right >= 0 and nums[right] >= k :
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                
                left += 1
                right -= 1
                
        return left
