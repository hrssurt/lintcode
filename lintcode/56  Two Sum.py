"""***************************  TITLE  ****************************"""
"""56  Two Sum.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array of integers, find two numbers such that they add up to a specific target number.
"""



"""***************************  EXAMPLES  ****************************"""
"""
twoSum
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if not numbers:
            return [-1, -1]
            
        idx_lst = [idx for idx, num in sorted(enumerate(numbers), key=lambda x: x[1])]
        numbers.sort()
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return sorted([idx_lst[left], idx_lst[right]])
            
            elif numbers[left] + numbers[right] > target:
                right -= 1
            
            else:
                left += 1
                
        return [-1, -1]
