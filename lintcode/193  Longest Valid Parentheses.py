"""***************************  TITLE  ****************************"""
"""193  Longest Valid Parentheses.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
"""



"""***************************  EXAMPLES  ****************************"""
"""
'('
"""



"""***************************  CODE  ****************************"""
class Solution:
    def longestValidParentheses(self, s):
        if not s:
            return 0
        dp = [0 for _ in range(len(s))]         # dp[i] represents the longest valid paranthes
                                                # starting from idx i
        for i in range(len(s)-2, -1, -1):       # loop from len(s) -2 to 0, inclusive, backward
            if s[i] == ')':
               dp[i] = 0                        # there is no valid string that start with )
            else:
                possible_end = i + dp[i+1] + 1
                if possible_end < len(s) and s[possible_end] == ')':
                    dp[i] = dp[i+1] + 2
                    
                    if possible_end+1 < len(s):
                        dp[i] += dp[possible_end+1]
            
        
        return max(dp)
        
