"""***************************  TITLE  ****************************"""
"""107  Word Break.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a string s and a dictionary of words dict, determine if s can be broken into a space-separated sequence of one or more dictionary words.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Example 1:
	Input:  "lintcode", ["lint", "code"]
	Output:  true

Example 2:
	Input: "a", ["a"]
	Output:  true
	

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        if not s:
            return True
            
        if not dict:
            return False
        
        dict = set(dict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in dict:
                    dp[i] = True
                    
        return dp[len(s)]
