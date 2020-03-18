"""***************************  TITLE  ****************************"""
"""58  4Sum.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:[2,7,11,15],3
Output:[]


"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        if not numbers or len(numbers) < 4:
            return []
        
        result = []
        numbers.sort()
        for i in range(len(numbers) - 3):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            
            for j in range(i+1, len(numbers) - 2):
                if j > i+1 and numbers[j] == numbers[j-1]:
                    continue
                
                left, right = j+1, len(numbers) - 1
                while left < right:
                    if left > j + 1 and numbers[left] == numbers[left-1]:
                        left += 1

                    elif numbers[i] + numbers[j] + numbers[left] + numbers[right] == target:
                        result.append(list(sorted([numbers[i], numbers[j], numbers[left],  numbers[right]])))
                        left += 1
                        right -= 1
                        
                    elif numbers[i] + numbers[j] + numbers[left] + numbers[right] > target:
                        right -= 1
                    
                    else:
                        left += 1
                        
        return result
