"""***************************  TITLE  ****************************"""
"""184  Largest Number.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a list of non negative integers, arrange them such that they form the largest number.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:[1, 20, 23, 4, 8]
Output:"8423201"

"""



"""***************************  CODE  ****************************"""
from functools import cmp_to_key
class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """

    
    def largestNumber(self, nums):
        # write your code here
        def cmp_f(n1, n2):
            return -1 if str(n1) + str(n2) < str(n2) + str(n1) else 1
            
        nums = reversed(sorted(nums, key = cmp_to_key(lambda x, y: cmp_f(x, y))))
        result = "".join([str(n) for n in nums])
        for c in result:
            if c != "0":
                return result
        return "0"    # deal with ["0", "0"]
