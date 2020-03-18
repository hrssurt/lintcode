"""***************************  TITLE  ****************************"""
"""837  Palindromic Substrings.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input: "abc"
Output: 3
Explanation:
3 palindromic strings: "a", "b", "c".

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, str):
        # write your code here
        if not str:
            return 0
        
        f = [[0 for _ in range(len(str))] for _ in range(len(str))]
        ans = 0
        for j in range(len(str)):
            for i in range(j+1):
                if str[i] == str[j]: 
                    if j - i <= 2 or f[i+1][j-1] == 1:
                        f[i][j] = 1
                ans += f[i][j]    
        return ans
        

