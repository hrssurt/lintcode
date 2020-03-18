"""***************************  TITLE  ****************************"""
"""539  Move Zeroes.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""



"""***************************  EXAMPLES  ****************************"""
"""
nums
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        if not nums: return
        target_idx, nonzero_idx = 0, 0   # nonzero_idx used to find the nonzero elements, and target_idx is where we should move it to
        
        while nonzero_idx < len(nums):
            if nums[nonzero_idx] != 0:
                nums[nonzero_idx], nums[target_idx] = nums[target_idx], nums[nonzero_idx]
                target_idx += 1
            
            nonzero_idx += 1
            
            
        
        
        

