"""***************************  TITLE  ****************************"""
"""1246  Longest Repeating Character Replacement.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.
"""



"""***************************  EXAMPLES  ****************************"""
"""
Input:
"ABAB"
2
Output:
4
Explanation:
Replace the two 'A's with two 'B's or vice versa.

"""



"""***************************  CODE  ****************************"""
class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        if not s: return 0
        if len(s) <= k: return len(s)
        
        
        left, right, d = 0, 0, {}
        max_result = 0
        for right in range(len(s)):
            d[s[right]] = d.get(s[right], 0) + 1
            substr_len = right - left + 1
            mxl = self.get_max(d)
            if substr_len - mxl <= k:
                max_result = max(max_result, substr_len)
            
            # keep moving the left pointer until    
            while substr_len - mxl > k and left <= right:
                d[s[left]] -= 1
                left += 1
                substr_len = right - left + 1
                mxl = self.get_max(d)

            

        return max_result
            
            
    
    
    def get_max(self, d):
        if not d:
            return 0
        return max([v for k, v in d.items()])
