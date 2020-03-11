class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # let dp[i] respresents the longest increasing subsequece that ends in nums[i]
        # meaning nums[i] is included in the sequence
        if not nums: return 0
        
        dp = [1 for _ in nums]
        max_len = 1
        for i in range(1, len(dp)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_len = max(max_len, dp[i])
                    
        return max_len