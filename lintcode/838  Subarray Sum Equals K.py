"""***************************  TITLE  ****************************"""
"""838  Subarray Sum Equals K.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: nums = [1,1,1] and k = 2
Output: 2
Explanation:
subarray [0,1] and [1,2]

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum         equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        if not nums:
            return 0
        d = {0:1}       # there is one way to get 0, which is take nothing
        
        result = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        for i in range(0,len(nums)):
            if nums[i] - k  in d:         
                  result += d[nums[i] - k]
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
         
        return result
