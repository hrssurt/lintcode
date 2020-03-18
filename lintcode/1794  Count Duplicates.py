"""***************************  TITLE  ****************************"""
"""1794  Count Duplicates.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array of integers, your task is to count the number of duplicate array elements. Duplicate is defined as two or more identical elements. For example, in the array[1, 2, 2, 3, 3, 3],the two twos are one duplicate and so are the three threes.you need return an array including every non-unique(duplicate) values in the numbers array (with the same order of given array).
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: nums = [1, 2, 2, 3, 3, 3]
Output: [2, 3]

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param nums: a integer array
    @return: return an integer denoting the number of non-unique(duplicate) values
    """
    def CountDuplicates(self, nums):
        if not nums:
            return nums
        d = {}
        result = []
        for n in nums:
            d[n] = d.get(n, 0) + 1
            if d[n] == 2:
                result.append(n)

        return result

            
