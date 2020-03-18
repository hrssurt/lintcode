"""***************************  TITLE  ****************************"""
"""57  3Sum.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""



"""***************************  EXAMPLES  ****************************"""
"""
a + b + c = 0
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers) < 3:
            return []
        
        numbers.sort()
        result = []
        for i in range(len(numbers) - 2):
            if i >= 1 and numbers[i] == numbers[i-1]:
                continue
            
            target = -numbers[i]
            left, right = i+1, len(numbers) - 1
            while left < right:
                if left > i + 1 and numbers[left] == numbers[left-1]:
                    left += 1   # prevent duplicates
                    
                elif numbers[left] + numbers[right] == target:
                    result.append(list(sorted([-target, numbers[left], numbers[right]])))
                    left += 1
                    right -= 1
                elif numbers[left] + numbers[right] > target:
                    right -= 1
                else:
                    left += 1
                    
        return result
                
