"""***************************  TITLE  ****************************"""
"""582  Word Break II.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input："lintcode"，["de","ding","co","code","lint"]
Output：["lint code", "lint co de"]
Explanation：
insert a space is "lint code"，insert two spaces is "lint co de".

"""



"""***************************  CODE  ****************************"""
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = list(set([x for x in wordDict if x]))
        cache = {}
        if not s or not wordDict:
            return []
            
        def dfs(target, cache):
            if target in cache:
                return cache[target]
            
            result = []
            if not target:
                return [[]]
                
            for word in wordDict:
                if target[0:len(word)] == word:
                    sub_results = dfs(target[len(word):], cache)
                    for sub in sub_results:
                        result.append([word] + sub)
                    cache[target] = result
                    
            return result
        
        result = dfs(s, cache)
        return [" ".join(lst) for lst in result]
