"""***************************  TITLE  ****************************"""
"""1221  Concatenated Words.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
"""



"""***************************  EXAMPLES  ****************************"""
"""
10,000
"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param words: List[str]
    @return: return List[str]
    """
    def findAllConcatenatedWordsInADict(self, words):
        result = []
        words = set(words)
        for word in words:
            if not word:
                continue
            words.remove(word)
            r = self.dp(word, words)
            words.add(word)
            if r:
                result.append(word)
        return result
                
                
    def dp(self, word, words):
        dp = [False for _ in range(len(word) + 1)]
        dp[0] = True
        for i in range(1, len(word) + 1):
            for j in range(0, i):
                if dp[j] and word[j: i] in words:
                    dp[i] = True
                    
        return dp[-1]
        
