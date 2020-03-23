"""***************************  TITLE  ****************************"""
"""7. Reverse Integer.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321


Example 2:

Input: -123
Output: -321


Example 3:

Input: 120
Output: 21


Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""



"""***************************  CODE  ****************************"""
class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        is_positive = x > 0
        x = abs(x)
        threshold = (2**31-1)
        
        while x:
            last_digit = x % 10
            x = x // 10
            
            r = r * 10 + last_digit
            if r > threshold: return 0
            
        if is_positive:
            return r
        else:
            return -r
            
            
            
        
​
