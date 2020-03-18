"""***************************  TITLE  ****************************"""
"""683  Word Break III.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Give a dictionary of words and a sentence with all whitespace removed, return the number of sentences you can form by inserting whitespaces to the sentence so that each word can be found in the dictionary.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:
"CatMat"
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
Output: 3
Explanation:
we can form 3 sentences, as follows:
"CatMat" = "Cat" + "Mat"
"CatMat" = "Ca" + "tM" + "at"
"CatMat" = "C" + "at" + "Mat"

"""



"""***************************  CODE  ****************************"""
class Solution:
    def wordBreak3(self, s, dict):
        if not s or not dict:
            return 0
            
        dict = set([x.lower() for x in dict])
        s = s.lower()
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if s[j:i] in dict:
                    dp[i] += dp[j]
                    
                    
        return dp[len(s)]
                    
