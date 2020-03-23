"""***************************  TITLE  ****************************"""
"""844. Backspace String Compare.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.


Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".



Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".



Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".



Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".


Note:


	1 <= S.length <= 200
	1 <= T.length <= 200
	S and T only contain lowercase letters and '#' characters.


Follow up:


	Can you solve it in O(N) time and O(1) space?






"""



"""***************************  CODE  ****************************"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if not t and not s: return True
        idx1 = len(s) - 1
        idx2 = len(t) - 1
        
        skip1 = skip2 = 0
        while idx1 >= 0 or idx2 >= 0:
            while idx1 >= 0:
                if s[idx1] == '#':
                    idx1 -= 1
                    skip1 += 1
                elif skip1 > 0:
                    skip1 -= 1
                    idx1 -= 1
                else:
                    break
                    
            while idx2 >= 0:
                if t[idx2] == '#':
                    idx2 -= 1
                    skip2 += 1
                elif skip2 > 0:
                    skip2 -= 1
                    idx2 -= 1
                else:
                    break
                    
            if (idx1 >= 0) != (idx2 >= 0):
                return False
            
            elif idx1 >= 0 and idx2 >= 0 and s[idx1] != t[idx2]:
                return False
            
            idx1 -= 1
            idx2 -= 1
        
        
        return True
                
                
                    
                
        
​
