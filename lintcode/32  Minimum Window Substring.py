"""***************************  TITLE  ****************************"""
"""32  Minimum Window Substring.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Given two strings source and target. Return the minimum substring of source which contains each char of target.
"""



"""***************************  EXAMPLES  ****************************"""
"""
source
"""



"""***************************  CODE  ****************************"""
class Solution:
    def minWindow(self, source , target):
        if not source or not target or len(source) < len(target):
            return ""
        dt, ds = {}, {}
        for char in target:
            dt[char] = dt.get(char, 0) + 1
        cur_min_match_length, match_count, left, right, min_str = float("inf"), 0, 0, 0, ""
       
        while right < len(source):
            while match_count < len(dt) and right < len(source):    # try to find a match by moving right
                char = source[right]
                ds[char] = ds.get(char, 0) + 1
                if char in dt and ds[char] == dt[char]:
                    match_count += 1
                right += 1
                
            if match_count == len(dt) and right - left + 1 < cur_min_match_length:
                cur_min_match_length = right - left + 1
                min_str = source[left: right]
                
            # now we have found a substring that contains all chars in the target
            # now we are trying to move the left pointer to reduce the substring size
            # when moving, we need to update the match_count, ds
            while left <= right and match_count == len(dt):
                if right - left + 1 < cur_min_match_length:
                    cur_min_match_length = right - left + 1
                    min_str = source[left:right]
                left_char = source[left]
                
                if left_char in dt and dt[left_char] == ds[left_char]:
                    match_count -= 1
                
                ds[left_char] -= 1
                left += 1
            
        
        return min_str
                    
