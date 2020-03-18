"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        lst = [int(c) for c in str(n)]
        if len(lst) <= 1:
            return -1
        
        if len(lst) == 2:
            if lst[0] >= lst[1]:
                return -1
            else:
                return int("".join([str(i) for i in lst[::-1]]))
        
        i = len(lst) - 1
        while i-1 >= 0 and lst[i-1] >= lst[i]:
            i -= 1
        
        if i == 0:
            return -1
        else:
            j = len(lst) - 1
            while j >= i:
                if lst[j] > lst[i-1]:
                    break
                j -= 1
            
            lst[i-1], lst[j] = lst[j], lst[i-1]
            lst = lst[:i] + sorted(lst[i:])
            new_n = int("".join([str(n) for n in lst]))
            return new_n if new_n <= 2 ** 31 else -1
            
        
        
        