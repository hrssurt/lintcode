"""***************************  TITLE  ****************************"""
"""627  Longest Palindrome.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
"""



"""***************************  EXAMPLES  ****************************"""
"""
"Aa"
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
            
        res = 0
        for v in d.values():
            res +=  v // 2 * 2
            
        return res if res == len(s) else res + 1

