"""***************************  TITLE  ****************************"""
"""344. Reverse String.py"""



"""***************************  DESCRIPTION  ****************************"""
"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 


Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]



Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]




"""



"""***************************  CODE  ****************************"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if not s: return
        start, end = 0, len(s) -1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            
        
        
​
