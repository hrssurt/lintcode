"""***************************  TITLE  ****************************"""
"""200  Longest Palindromic Substring.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""



"""***************************  EXAMPLES  ****************************"""
"""
S
"""



"""***************************  CODE  ****************************"""
class Solution:
    def longestPalindrome(self, s):
        if not s or len(s) <= 1:
            return s
        
        def find_longest_pstr(left, right, s, cur_str):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cur_str = s[left] + cur_str + s[right]
                left -= 1
                right += 1
            return cur_str
        
        max_str, max_len = "", 0
        for mid in range(len(s)):
            # first, try string with even length
            left, right = mid, mid+1
            cur_str = find_longest_pstr(left, right, s, "")
            if len(cur_str) > max_len:
                max_len, max_str = len(cur_str), cur_str
            
            # second, try the string with odd length
            left, right = mid -1, mid+1
            cur_str = find_longest_pstr(left, right, s, s[mid])
            if len(cur_str) > max_len:
                max_len, max_str = len(cur_str), cur_str
            


        return max_str
