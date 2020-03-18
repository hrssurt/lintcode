"""***************************  TITLE  ****************************"""
"""1281  Top K Frequent Elements.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a non-empty array of integers, return the k most frequent elements.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        if not nums:
            return []
            
        if k >= len(nums):
            return list(set(nums))
        
        d = {}    
        for n in nums:
            d[n] = d.get(n, 0) + 1
            
        vk_pairs = sorted([(v,k) for k,v in d.items()], reverse = True)[:k]
        return [p[1] for p in vk_pairs]
