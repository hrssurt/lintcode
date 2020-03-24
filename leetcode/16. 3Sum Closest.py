"""***************************  TITLE  ****************************"""
"""16. 3Sum Closest.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


"""



"""***************************  CODE  ****************************"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) <= 2:
            return -1
        
        result = nums[0] + nums[1] + nums[-1]
        nums.sort()
        
        for i in range(0, len(nums)):
            left, right = i +1, len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right] + nums[i]
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    return target
                
                
                
                if abs(cur_sum - target) < abs(result - target):
                    result = cur_sum
                    
        return result
        
        
​
