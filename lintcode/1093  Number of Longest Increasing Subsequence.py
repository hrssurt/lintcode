"""***************************  TITLE  ****************************"""
"""1093  Number of Longest Increasing Subsequence.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an unsorted array of integers, find the number of longest increasing subsequence.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param nums: an array
    @return: the number of longest increasing subsequence
    """
    def findNumberOfLIS(self, nums):
        # let dp[i] respresents the longest increasing subsequece that ends in nums[i]
        # meaning nums[i] is included in the sequence
        if not nums: return 0
        
        dp = [1 for _ in nums]
        ans = [1 for _ in nums]
        
        max_len = 1
        for i in range(1, len(dp)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[i] == dp[j] + 1:  # same sequence
                        ans[i] += ans[j]
                    elif dp[i] < dp[j]  + 1:
                        ans[i] = ans[j]
                        dp[i] = dp[j] + 1
            max_len = max(dp[i], max_len)            
            
        
        return sum([y for x, y in zip(dp, ans) if x == max_len])

