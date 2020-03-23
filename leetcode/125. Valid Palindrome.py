"""***************************  TITLE  ****************************"""
"""125. Valid Palindrome.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true


Example 2:

Input: "race a car"
Output: false


"""



"""***************************  CODE  ****************************"""
import string
​
​
​
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        l = set([c for c in string.ascii_lowercase] + [str(n) for n in range(0,10)])
        s = s.lower()
        start, end = 0, len(s) -1 
        while start < end:
            while start < end and s[start] not in l:
                start += 1
            
            while start < end and s[end] not in l:
                end -= 1
                
            if start >= end:
                break
            
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
            
        return True
        
​
