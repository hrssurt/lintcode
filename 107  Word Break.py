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
        
        dict = list(set([word.lower() for word in dict]))
        def dfs(target, dict):
            if not target:
                return True
            
            for word in dict:
                if target[0:len(word)] == word:
                    searchResult = dfs(target[len(word):], dict)
                    if searchResult:
                        return True
                        
            return False
                
                
        return dfs(s, dict)
