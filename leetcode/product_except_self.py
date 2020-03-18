class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 1
        left_product = [1 for _ in range(len(nums))]  # ith is the cumlative products i-1
        right_product = [1 for _ in range(len(nums))]
        
        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]
            
        return [left_product[i] * right_product[i] for i in range(len(nums))]
        